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
        input = '6\n3 1 2 4 2 1'
        output = '2'
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = '4\n1 2 3 4'
        output = '0'
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = '10\n3 3 3 3 4 4 4 5 5 5'
        output = '20'
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    l1 = l2 = 0
    for i in range(1, N):
        if l1 == 0:
            if A[i] == A[i - 1]:
                l1 = A[i - 1]
        elif i < N - 1 and A[i + 1] == A[i]:
            l2 = A[i]
            break
    print(l1 * l2)


def __starting_point():
    resolve()


__starting_point()
