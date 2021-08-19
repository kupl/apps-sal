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
        input = '4 5'
        output = 'Possible'
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = '1 1'
        output = 'Impossible'
        self.assertIO(input, output)


def resolve():
    (A, B) = list(map(int, input().split()))
    if A % 3 == 0 or B % 3 == 0 or (A + B) % 3 == 0:
        print('Possible')
    else:
        print('Impossible')


def __starting_point():
    resolve()


__starting_point()
