import sys


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    used = set()
    Ans = [None for _ in range(M)]
    left = 1
    right = N
    for i in range(M):
        if right - left in used or 2 * (right - left) == N:
            right -= 1
        Ans[i] = (left, right)
        diff = right - left
        used |= {diff, N - diff}
        left += 1
        right -= 1
    for i in range(M):
        print(*Ans[i], sep=" ")

    return 0


def __starting_point():
    solve()


__starting_point()
