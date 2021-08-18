
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
        input = """3"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """999999999"""
        output = """1999999998"""
        self.assertIO(input, output)


def resolve():
    N = int(input())

    if N % 2 == 0:
        print(N)
    else:
        print((N * 2))


def __starting_point():
    resolve()


__starting_point()
