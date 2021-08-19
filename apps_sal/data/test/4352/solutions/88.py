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
        input = '8 6'
        output = 'Alice'
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = '1 1'
        output = 'Draw'
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = '13 1'
        output = 'Bob'
        self.assertIO(input, output)


def resolve():
    (A, B) = list(map(int, input().split()))
    if A == 1:
        A = 14
    if B == 1:
        B = 14
    if A > B:
        print('Alice')
    elif A < B:
        print('Bob')
    else:
        print('Draw')


def __starting_point():
    resolve()


__starting_point()
