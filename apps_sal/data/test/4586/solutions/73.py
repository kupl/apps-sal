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
        input = '1118'
        output = 'Yes'
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = '7777'
        output = 'Yes'
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = '1234'
        output = 'No'
        self.assertIO(input, output)


def resolve():
    N = input()
    if N[0] == N[1] == N[2] or N[1] == N[2] == N[3]:
        print('Yes')
    else:
        print('No')


def __starting_point():
    resolve()


__starting_point()
