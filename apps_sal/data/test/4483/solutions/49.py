#
# abc087 a
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
        input = """1234
150
100"""
        output = """84"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000
108
108"""
        output = """28"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """579
123
456"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """7477
549
593"""
        output = """405"""
        self.assertIO(input, output)


def resolve():
    X = int(input())
    A = int(input())
    B = int(input())

    print(((X-A) % B))


def __starting_point():
    # unittest.main()
    resolve()

__starting_point()
