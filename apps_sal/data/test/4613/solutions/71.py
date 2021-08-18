import sys
from io import StringIO
import unittest
from collections import deque


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
        input = """7 7
1 3
2 7
3 4
4 5
4 6
5 6
6 7"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3
1 2
1 3
2 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 5
1 2
2 3
3 4
4 5
5 6"""
        output = """5"""
        self.assertIO(input, output)


def resolve():
    N, M = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]

    ans = 0
    for i in range(M):
        Target = AB[:]
        Target.pop(i)

        G = [[i + 1, 0] for i in range(N)]
        for ab in Target:
            a, b = ab
            G[a - 1][1] += 1
            G[b - 1][1] += 1
            G[a - 1].append(b)
            G[b - 1].append(a)

        F = [False] * N
        Q = deque()
        Q.append(1)
        F[0] = True

        while Q:
            p = Q.pop()
            if G[p - 1][1] == 0:
                continue

            for np in G[p - 1][2:]:
                if F[np - 1]:
                    continue
                Q.append(np)
                F[np - 1] = True

        for f in F:
            if f == False:
                ans += 1
                break

    print(ans)


def __starting_point():
    resolve()


__starting_point()
