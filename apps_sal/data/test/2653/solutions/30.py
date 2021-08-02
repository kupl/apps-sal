#
# abc138 d
#
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
        input = """4 3
1 2
2 3
2 4
2 10
1 100
3 1"""
        output = """100 110 111 110"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 2
1 2
1 3
2 4
3 6
2 5
1 10
1 10"""
        output = """20 20 20 20 20 20"""
        self.assertIO(input, output)


def resolve():
    N, Q = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(N - 1)]
    PX = [list(map(int, input().split())) for _ in range(Q)]

    G = [[i + 1, 0] for i in range(N)]
    for ab in AB:
        a, b = ab
        G[a - 1][1] += 1
        G[b - 1][1] += 1
        G[a - 1].append(b)
        G[b - 1].append(a)

    ans = [0] * N
    for px in PX:
        p, x = px
        ans[p - 1] += x

    S = deque()

    F = [False] * N
    S.append(1)
    F[0] = True

    while S:
        p = S.pop()
        if G[p - 1][1] == 0:
            continue

        for np in G[p - 1][2:]:
            if F[np - 1]:
                continue
            S.append(np)
            F[np - 1] = True
            ans[np - 1] += ans[p - 1]

    print((*ans))


def __starting_point():
    # unittest.main()
    resolve()


__starting_point()
