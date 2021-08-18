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
        input = """1
24 30"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
6 8
3 3"""
        output = """4"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for lr in LR:
        l, r = lr
        ans += r - l + 1

    print(ans)


def __starting_point():
    resolve()


__starting_point()
