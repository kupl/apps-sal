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
        input = """100 17"""
        output = """83"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """48 58"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000 1000000000"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    X, t = list(map(int, input().split()))
    print((max(X - t, 0)))


def __starting_point():
    resolve()


__starting_point()
