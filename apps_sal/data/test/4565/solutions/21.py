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
        input = '5\nWEEWW'
        output = '1'
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = '12\nWEWEWEEEWWWE'
        output = '4'
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = '8\nWWWWWEEE'
        output = '3'
        self.assertIO(input, output)


def resolve():
    N = int(input())
    S = list(input())
    W = [0] * N
    E = [0] * N
    L = 0
    R = 0
    for i in range(N):
        if S[i] == 'W':
            L += 1
        if S[N - 1 - i] == 'E':
            R += 1
        W[i] = L
        E[N - 1 - i] = R
    ans = float('inf')
    for i in range(N):
        ans = min(ans, E[i] + W[i] - 1)
    print(ans)


def __starting_point():
    resolve()


__starting_point()
