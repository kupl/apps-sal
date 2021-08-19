import sys
from io import StringIO
import unittest
from collections import Counter


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
        input = '6\nG W Y P Y W'
        output = 'Four'
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = '9\nG W W G P W P G G'
        output = 'Three'
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = '8\nP Y W G Y W Y Y'
        output = 'Four'
        self.assertIO(input, output)


def resolve():
    N = int(input())
    S = list(input().split())
    C = Counter(S)
    if 'Y' in C:
        print('Four')
    else:
        print('Three')


def __starting_point():
    resolve()


__starting_point()
