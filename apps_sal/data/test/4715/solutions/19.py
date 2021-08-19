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
        input = '3 1 4'
        output = '3'
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = '3 3 33'
        output = '2'
        self.assertIO(input, output)


def resolve():
    (a, b, c) = list(map(int, input().split()))
    ans = 0
    if a == b == c:
        print('1')
    elif a == b or b == c or c == a:
        print('2')
    else:
        print('3')


def __starting_point():
    resolve()


__starting_point()
