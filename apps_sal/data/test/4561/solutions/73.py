
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
        input = """4 3 6"""
        output = """safe"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 5 1"""
        output = """delicious"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 7 12"""
        output = """dangerous"""
        self.assertIO(input, output)


def resolve():
    X, A, B = list(map(int, input().split()))

    if A - B >= 0:
        print("delicious")
    elif B - A <= X:
        print("safe")
    else:
        print("dangerous")


def __starting_point():
    resolve()


__starting_point()
