#
# abc096 a
#
import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """3 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 -2"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0 0"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    A, B = list(map(int, input().split()))

    print((max(A + B, A - B, A * B)))


def __starting_point():
    # unittest.main()
    resolve()


__starting_point()
