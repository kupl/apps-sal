#
# abc047 c
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
        input = """BBBWW"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """WWWWWW"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """WBWBWBWBWB"""
        output = """9"""
        self.assertIO(input, output)


def resolve():
    S = list(input())

    i = 1
    while i < len(S):
        if S[i] == S[i - 1]:
            del S[i]
        else:
            i += 1

    print((len(S) - 1))


def __starting_point():
    # unittest.main()
    resolve()


__starting_point()
