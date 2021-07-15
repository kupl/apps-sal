#
# abc080 c
#
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
        input = """1
1 1 0 1 0 0 0 1 0 1
3 4 5 6 7 8 9 -2 -3 4 -2"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1
0 -2 -2 -2 -2 -2 -1 -1 -1 -1 -1
0 -2 -2 -2 -2 -2 -1 -1 -1 -1 -1"""
        output = """-2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
1 1 1 1 1 1 0 0 1 1
0 1 0 1 1 1 1 0 1 0
1 0 1 1 0 1 0 1 0 1
-8 6 -2 -8 -8 4 8 7 -6 2 2
-9 2 0 1 7 -5 0 -2 -6 5 5
6 -6 7 -9 6 -5 8 0 -9 -7 -7"""
        output = """23"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    F = [list(map(int, input().split())) for _ in range(N)]
    P = [list(map(int, input().split())) for _ in range(N)]

    ans = sum([min(p) for p in P])
    for bit in range(1, 1 << 10):
        lbit = list(map(int, format(bit, "b").zfill(10)))
        p = 0
        for i, f in enumerate(F):
            n = 0
            for j in range(10):
                if lbit[j] == f[j] == 1:
                    n += 1
            p += P[i][n]
        ans = max(ans, p)

    print(ans)


def __starting_point():
    # unittest.main()
    resolve()

__starting_point()
