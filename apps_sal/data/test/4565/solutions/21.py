#
# abc096 c
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
        input = """5
WEEWW"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """12
WEWEWEEEWWWE"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8
WWWWWEEE"""
        output = """3"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    S = list(input())

#    ans = float("inf")
#    for i in range(N):
#        if i == 0:
#            ans = min(ans, S[1:].count("E"))
#        elif i == N-1:
#            ans = min(ans, S[0:N-1].count("W"))
#        else:
#            ans = min(ans, S[0:i].count("W") + S[i+1:].count("E"))
#    print(ans)

    W = [0] * N
    E = [0] * N
    L = 0
    R = 0

    for i in range(N):
        if S[i] == "W":
            L += 1
        if S[N-1-i] == "E":
            R += 1
        W[i] = L
        E[N-1-i] = R

    ans = float("inf")
    for i in range(N):
        ans = min(ans, E[i]+W[i]-1)
    print(ans)


def __starting_point():
    # unittest.main()
    resolve()

__starting_point()
