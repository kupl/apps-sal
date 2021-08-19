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
        input = '50 100 120'
        output = 'Yes'
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = '500 100 1000'
        output = 'No'
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = '19 123 143'
        output = 'No'
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = '19 123 142'
        output = 'Yes'
        self.assertIO(input, output)


def resolve():
    (A, B, C) = list(map(int, input().split()))
    if A + B >= C:
        print('Yes')
    else:
        print('No')


def __starting_point():
    resolve()


__starting_point()
