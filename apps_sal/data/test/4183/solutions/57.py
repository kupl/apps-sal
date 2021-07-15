#
# abc070 c
#
import sys
from io import StringIO
import unittest
import math
from functools import reduce


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
        input = """2
2
3"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
2
5
10
1000000000000000000
1000000000000000000"""
        output = """1000000000000000000"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    T = [int(input()) for _ in range(N)]

    print((lcmlist(T)))


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


def lcmlist(l):
    return reduce(lcm, l)


def __starting_point():
    # unittest.main()
    resolve()

__starting_point()
