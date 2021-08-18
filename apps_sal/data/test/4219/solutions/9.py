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
        input = """3
1
2 1
1
1 1
1
2 0"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
2
2 1
3 0
2
3 1
1 0
2
1 1
2 0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
1
2 0
1
1 0"""
        output = """1"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    C = []
    for i in range(N):
        a = int(input())
        C.append([list(map(int, input().split())) for j in range(a)])

    ans = 0
    for bit in range(1 << N):
        f = True
        for i in range(N):
            if bit & (1 << i):
                for c in C[i]:
                    if bit & (1 << c[0] - 1) != (1 << c[0] - 1) * c[1]:
                        f = False
                        break
        if f == True:
            ans = max(ans, bin(bit).count("1"))
    print(ans)


def __starting_point():
    resolve()


__starting_point()
