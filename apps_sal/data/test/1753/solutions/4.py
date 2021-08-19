import sys
import math
3
DEBUG = False


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(N, M, A):
    ans = [[] for _ in range(N)]
    for i in range(1, N + 1):
        ans[i - 1].append((i, i))
    y = N + 1
    for a in range(1, N + 1):
        for b in range(a + 1, N + 1):
            if A[a][b] == 1:
                ans[a - 1].append((a, y))
                ans[b - 1].append((b, y))
                y += 1
    return ans


def main():
    (N, M) = [int(e) for e in inp().split()]
    A = [bytearray(N + 1) for _ in range(N + 1)]
    for _ in range(M):
        (a, b) = [int(e) for e in inp().split()]
        A[a][b] = 1
        A[b][a] = 1
    ans = solve(N, M, A)
    assert len(ans) == N
    for coords in ans:
        print(len(coords))
        for (x, y) in coords:
            print(x, y)


def __starting_point():
    main()


__starting_point()
