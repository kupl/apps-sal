#
# abc136 a
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
        input = """6 4 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8 3 9"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """12 3 7"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    A, B, C = list(map(int, input().split()))

    print((max(C-(A-B), 0)))


def __starting_point():
    # unittest.main()
    resolve()

__starting_point()
