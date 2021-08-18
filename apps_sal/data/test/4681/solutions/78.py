import sys
from io import StringIO
import unittest
from functools import lru_cache

sys.setrecursionlimit(10**9)


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
        input = """5"""
        output = """11"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """86"""
        output = """939587134549734843"""
        self.assertIO(input, output)


def resolve():
    N = int(input())

    print((L(N)))


@lru_cache(maxsize=1000)
def L(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return L(n - 1) + L(n - 2)


def __starting_point():
    resolve()


__starting_point()
