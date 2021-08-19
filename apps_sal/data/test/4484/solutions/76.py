import sys
from io import StringIO
import unittest
import math


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
        input = '2 2'
        output = '8'
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = '3 2'
        output = '12'
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = '1 8'
        output = '0'
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = '100000 100000'
        output = '530123477'
        self.assertIO(input, output)


def resolve():
    (N, M) = list(map(int, input().split()))
    if abs(N - M) > 1:
        print('0')
    elif N == M:
        print(2 * math.factorial(N) * math.factorial(M) % (10 ** 9 + 7))
    else:
        print(math.factorial(N) * math.factorial(M) % (10 ** 9 + 7))


def __starting_point():
    resolve()


__starting_point()
