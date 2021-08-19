#
# abc080 a
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
        input = """7 17 120"""
        output = """119"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 20 100"""
        output = """100"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 18 100"""
        output = """100"""
        self.assertIO(input, output)


def resolve():
    N, A, B = list(map(int, input().split()))
    print((min(N * A, B)))


def __starting_point():
    # unittest.main()
    resolve()


__starting_point()
