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
        input = """5
MASHIKE
RUMOI
OBIRA
HABORO
HOROKANAI"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
ZZ
ZZZ
Z
ZZZZZZZZZZ"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
CHOKUDAI
RNG
MAKOTO
AOKI
RINGO"""
        output = """7"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    S = [input() for _ in range(N)]

    C = [0] * 5
    for s in S:
        if s[0] == "M":
            C[0] += 1
        elif s[0] == "A":
            C[1] += 1
        elif s[0] == "R":
            C[2] += 1
        elif s[0] == "C":
            C[3] += 1
        elif s[0] == "H":
            C[4] += 1

    ans = 0
    for i, c1 in enumerate(C):
        for j, c2 in enumerate(C[i + 1:], i + 1):
            for c3 in C[j + 1:]:
                ans += c1 * c2 * c3

    print(ans)


def __starting_point():
    resolve()


__starting_point()
