#
# abc059 b
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
        input = """36
24"""
        output = """GREATER"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """850
3777"""
        output = """LESS"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9720246
22516266"""
        output = """LESS"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """123456789012345678901234567890
234567890123456789012345678901"""
        output = """LESS"""
        self.assertIO(input, output)


def resolve():
    A = int(input())
    B = int(input())

    if A > B:
        print("GREATER")
    elif A < B:
        print("LESS")
    else:
        print("EQUAL")


def __starting_point():
    # unittest.main()
    resolve()

__starting_point()
