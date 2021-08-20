import sys
from io import StringIO
import unittest
import bisect


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
        input = '2\n1 5\n2 4\n3 6'
        output = '3'
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = '3\n1 1 1\n2 2 2\n3 3 3'
        output = '27'
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = '6\n3 14 159 2 6 53\n58 9 79 323 84 6\n2643 383 2 79 50 288'
        output = '87'
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort()
    B.sort()
    C.sort()
    ans = 0
    for b in B:
        an = bisect.bisect_left(A, b)
        cn = N - bisect.bisect_right(C, b)
        ans += an * cn
    print(ans)


def __starting_point():
    resolve()


__starting_point()
