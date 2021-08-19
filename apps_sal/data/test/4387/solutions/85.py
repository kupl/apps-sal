#
# abc104 a
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
        input = """1199"""
        output = """ABC"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1200"""
        output = """ARC"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4208"""
        output = """AGC"""
        self.assertIO(input, output)


def resolve():
    R = int(input())

    if R < 1200:
        print("ABC")
    elif R < 2800:
        print("ARC")
    else:
        print("AGC")


def __starting_point():
    # unittest.main()
    resolve()


__starting_point()
