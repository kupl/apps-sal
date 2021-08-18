import sys
from collections import defaultdict


def solve():
    input = sys.stdin.readline
    H, W, N = map(int, input().split())
    C = defaultdict(int)
    for _ in range(N):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        for h in range(3):
            for w in range(3):
                if 0 <= a - h < H - 2 and 0 <= b - w < W - 2:
                    C[(a - h, b - w)] += 1

    ans = [0] * 10
    s = 0
    for key in C:
        ans[C[key]] += 1
        s += 1
    ans[0] = ((H - 2) * (W - 2) - s)
    print(*ans, sep="\n")

    return 0


def __starting_point():
    solve()


__starting_point()
