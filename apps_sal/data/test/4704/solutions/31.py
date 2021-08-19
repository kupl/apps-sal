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
        input = '6\n1 2 3 4 5 6'
        output = '1'
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = '2\n10 -10'
        output = '20'
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = float('inf')
    S = sum(A)
    T = []
    T.append(A[0])
    for i in range(1, N):
        T.append(T[i - 1] + A[i])
    if N == 2:
        ans = abs(A[0] - A[1])
    else:
        for i in range(1, N - 1):
            ans = min(ans, abs(S - 2 * T[i]))
    print(ans)


def __starting_point():
    resolve()


__starting_point()
