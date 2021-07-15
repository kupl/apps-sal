import sys
from itertools import accumulate

input = sys.stdin.readline


def solve(H, W, D, A, Q, LR):
    position = [None] * (H * W + 1)
    for h in range(H):
        for w in range(W):
            position[A[h][w]] = (h, w)

    mp = [0] * (H * W + 1)

    for i in range(1, H * W + 1 - D):
        h, w = position[i]
        y, x = position[i + D]
        mp[i + D] = abs(x - w) + abs(y - h)

    for d in range(1, D + 1):
        mp[d::D] = list(accumulate(mp[d::D]))

    ans = [str(mp[r] - mp[l]) for l, r in LR]
    ans = "\n".join(ans)
    return ans


def main():
    H, W, D = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(H)]
    Q = int(input())
    LR = [list(map(int, input().split())) for _ in range(Q)]

    ans = solve(H, W, D, A, Q, LR)
    print(ans)


def __starting_point():
    main()

__starting_point()
