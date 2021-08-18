
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
        input = """1 6"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """12345 678901"""
        output = """175897"""
        self.assertIO(input, output)


def resolve():
    N, M = list(map(int, input().split()))

    if M >= 2 * N:
        print((N + (M - 2 * N) // 4))
    else:
        print((M // 2))


def __starting_point():
    resolve()


__starting_point()
