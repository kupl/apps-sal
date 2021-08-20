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
        input = 'AtCoder Beginner Contest'
        output = 'ABC'
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = 'AtCoder Snuke Contest'
        output = 'ASC'
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = 'AtCoder X Contest'
        output = 'AXC'
        self.assertIO(input, output)


def resolve():
    S = list(input().split())
    print('A' + S[1][0] + 'C')


def __starting_point():
    resolve()


__starting_point()
