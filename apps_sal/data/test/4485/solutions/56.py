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
        input = """3 2
1 2
2 3"""
        output = """POSSIBLE"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 3
1 2
2 3
3 4"""
        output = """IMPOSSIBLE"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100000 1
1 99999"""
        output = """IMPOSSIBLE"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """5 5
1 3
4 5
2 3
2 4
1 4"""
        output = """POSSIBLE"""
        self.assertIO(input, output)


def resolve():
    N, M = list(map(int, input().split()))
    S = [0] * N
    E = [0] * N
    for i in range(M):
        a, b = list(map(int, input().split()))
        if a == 1:
            S[b - 1] = 1
        if b == N:
            E[a - 1] = 1

    ans = "IMPOSSIBLE"
    for i in range(N):
        if S[i] == E[i] == 1:
            ans = "POSSIBLE"
            break
    print(ans)


def __starting_point():
    resolve()


__starting_point()
