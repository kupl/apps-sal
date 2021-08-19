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
        input = '100'
        output = 'ABC100'
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = '425'
        output = 'ABC425'
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = '999'
        output = 'ABC999'
        self.assertIO(input, output)


def resolve():
    print('ABC' + input())


def __starting_point():
    resolve()


__starting_point()
