3

import math
import sys


DEBUG = False


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(H, W, A):
    visited = [bytearray(W) for _ in range(H)]

    for y in range(H):
        for x in range(W):
            if A[y][x] == '.' or visited[y][x]:
                continue

            dprint(x, y)
            for dx, dy in [(0, 0), (-1, 0), (-2, 0),
                           (0, -1), (-2, -1),
                           (0, -2), (-1, -2), (-2, -2)]:
                tx = x + dx
                ty = y + dy
                dprint('  ', tx, ty)
                if tx < 0 or ty < 0 or tx + 2 >= W or ty + 2 >= H:
                    continue
                bad = False
                for ex, ey in [(0, 0), (1, 0), (2, 0),
                               (0, 1), (2, 1),
                               (0, 2), (1, 2), (2, 2)]:
                    nx = tx + ex
                    ny = ty + ey
                    if A[ny][nx] == '.':
                        bad = True
                        break
                if bad:
                    continue

                for ex, ey in [(0, 0), (1, 0), (2, 0),
                               (0, 1), (2, 1),
                               (0, 2), (1, 2), (2, 2)]:
                    nx = tx + ex
                    ny = ty + ey
                    visited[ny][nx] = 1

                assert visited[ny][nx] == 1
                break

            if visited[y][x] == 0:
                return False

    return True


def main():
    H, W = [int(e) for e in inp().split()]
    A = [inp() for _ in range(H)]

    print('YES' if solve(H, W, A) else 'NO')


def __starting_point():
    main()

__starting_point()
