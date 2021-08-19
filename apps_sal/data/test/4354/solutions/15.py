import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):

    def assertIO(self, input, output):
        (stdout, stdin) = (sys.stdout, sys.stdin)
        (sys.stdout, sys.stdin) = (StringIO(), StringIO(input))
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        (sys.stdout, sys.stdin) = (stdout, stdin)
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = '2 2\n2 0\n0 0\n-1 0\n1 0'
        output = '2\n1'
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = '3 4\n10 10\n-10 -10\n3 3\n1 2\n2 3\n3 5\n3 5'
        output = '3\n1\n2'
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = '5 5\n-100000000 -100000000\n-100000000 100000000\n100000000 -100000000\n100000000 100000000\n0 0\n0 0\n100000000 100000000\n100000000 -100000000\n-100000000 100000000\n-100000000 -100000000'
        output = '5\n4\n3\n2\n1'
        self.assertIO(input, output)


def resolve():
    (N, M) = list(map(int, input().split()))
    S = [list(map(int, input().split())) for _ in range(N)]
    C = [list(map(int, input().split())) for _ in range(M)]
    ans = []
    for s in S:
        D = float('inf')
        t = 0
        for i in range(M):
            d = abs(s[0] - C[i][0]) + abs(s[1] - C[i][1])
            if d < D:
                D = d
                t = i
        ans.append(t + 1)
    for a in ans:
        print(a)


def __starting_point():
    resolve()


__starting_point()
