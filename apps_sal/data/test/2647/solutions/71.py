#
# abc088 d
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
        input = """3 3
..#
# ..
..."""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 37
.....................................
...#...####...####..###...###...###..
..#.#..#...#.##....#...#.#...#.#...#.
..#.#..#...#.#.....#...#.#...#.#...#.
.#...#.#..##.#.....#...#.#.###.#.###.
.#####.####..#.....#...#..##....##...
.#...#.#...#.#.....#...#.#...#.#...#.
.#...#.#...#.##....#...#.#...#.#...#.
.#...#.####...####..###...###...###..
....................................."""
        output = """209"""
        self.assertIO(input, output)


def resolve():
    H, W = list(map(int, input().split()))
    S = [list(input()) for _ in range(H)]

    F = [[-1] * W for _ in range(H)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    Q = deque()
    Q.append([0, 0])
    F[0][0] = 1

    while Q:
        p = Q.popleft()
        x, y = p

        if x == W - 1 and y == H - 1:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= W or ny < 0 or ny >= H or S[ny][nx] == "#" or F[ny][nx] != -1:
                continue

            Q.append([nx, ny])
            F[ny][nx] = F[y][x] + 1

    if F[H - 1][W - 1] == -1:
        print((-1))
    else:
        NS = 0
        for s in S:
            NS += s.count("#")
        print((W * H - F[H - 1][W - 1] - NS))


def __starting_point():
    # unittest.main()
    resolve()


__starting_point()
