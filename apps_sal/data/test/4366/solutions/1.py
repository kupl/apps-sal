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
        input = '9 12'
        output = '21'
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = '19 0'
        output = '19'
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = '23 2'
        output = '1'
        self.assertIO(input, output)


def resolve():
    (A, B) = list(map(int, input().split()))
    print((A + B) % 24)


def __starting_point():
    resolve()


__starting_point()
