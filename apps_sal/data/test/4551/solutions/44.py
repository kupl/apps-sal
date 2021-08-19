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
        input = '3 8 7 1'
        output = 'Left'
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = '3 4 5 2'
        output = 'Balanced'
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = '1 7 6 4'
        output = 'Right'
        self.assertIO(input, output)


def resolve():
    (A, B, C, D) = list(map(int, input().split()))
    if A + B > C + D:
        print('Left')
    elif A + B < C + D:
        print('Right')
    else:
        print('Balanced')


def __starting_point():
    resolve()


__starting_point()
