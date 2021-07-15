#
# abc053 a
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
        input = """1000"""
        output = """ABC"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2000"""
        output = """ARC"""
        self.assertIO(input, output)


def resolve():
    x = int(input())

    if x < 1200:
        print("ABC")
    else:
        print("ARC")


def __starting_point():
    # unittest.main()
    resolve()

__starting_point()
