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
        input = """5 5"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """11 30"""
        output = """11"""
        self.assertIO(input, output)


def resolve():
    a, b = list(map(int, input().split()))

    if a > b:
        print((a-1))
    else:
        print(a)


def __starting_point():
    # unittest.main()
    resolve()

__starting_point()
