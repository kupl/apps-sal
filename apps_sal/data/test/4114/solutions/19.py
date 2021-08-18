import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """4
2 3 5
2 1 5
1 2 5
3 2 5"""
        output = """2 2 6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
0 0 100
1 1 98"""
        output = """0 0 100"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
99 1 191
100 1 192
99 0 192"""
        output = """100 0 193"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """4
59 3 0
64 94 56
5 62 11
3 93 14"""
        output = """55 80 79"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    XYH = [list(map(int, input().split())) for _ in range(N)]
    XYH.sort(key=lambda x: x[2], reverse=True)

    CX = CY = H = 0
    flag = False
    for cx in range(101):
        if flag == True:
            break
        for cy in range(101):
            H = XYH[0][2] + abs(XYH[0][0] - cx) + abs(XYH[0][1] - cy)
            for xyh in XYH[1:]:
                x, y, h = xyh
                if h != max(H - abs(x - cx) - abs(y - cy), 0):
                    break
            else:
                flag = True
                CX = cx
                CY = cy
                break

    print(f"{CX} {CY} {H}")


def __starting_point():
    resolve()


__starting_point()
