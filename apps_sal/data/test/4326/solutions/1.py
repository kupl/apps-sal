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
        input = """8"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9"""
        output = """3"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    print((N // 3))


def __starting_point():
    resolve()


__starting_point()
