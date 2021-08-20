import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    dx = []
    dy = []
    for _ in range(N):
        (x, y) = map(int, input().split())
        dx.append(x + y)
        dy.append(x - y)
    dx.sort()
    dy.sort()
    print(max(dx[N - 1] - dx[0], dy[N - 1] - dy[0]))
    return


def __starting_point():
    solve()


__starting_point()
