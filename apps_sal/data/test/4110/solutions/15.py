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
        input = """2 700
3 500
5 800"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2000
3 500
5 800"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 400
3 500
5 800"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """5 25000
20 1000
40 1000
50 1000
30 1000
1 1000"""
        output = """66"""
        self.assertIO(input, output)


def resolve():
    D, G = list(map(int, input().split()))
    PC = [list(map(int, input().split())) for _ in range(D)]

    ans = float("inf")
    for bit in range(1 << D):
        s = 0
        c = 0
        un = set(range(D))
        for i in range(D):
            if bit & 1 << i:
                s += 100 * (i + 1) * PC[i][0] + PC[i][1]
                c += PC[i][0]
                un.discard(i)

        if s >= G:
            ans = min(ans, c)
        else:
            u = max(un)
            for i in range(1, PC[u][0]):
                if s + (u + 1) * 100 * i >= G:
                    c += i
                    break
            else:
                continue
            ans = min(ans, c)

    print(ans)


def __starting_point():
    resolve()


__starting_point()
