import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    H, W, K = NMI()
    dp = make_grid(H + 1, W, 0)
    move = make_grid(W, W, 0)

    dp[0][0] = 1

    for case in range(2**(W - 1)):
        bad_case = False
        prev_bit = -1
        for i in range(W - 1):
            now_bit = (case >> i) & 1
            if now_bit == prev_bit == 1:
                bad_case = True
            prev_bit = now_bit
        if bad_case:
            continue

        for b in range(W):

            if b == 0:
                if (case >> 0) & 1:
                    move[0][1] += 1
                else:
                    move[0][0] += 1

            elif b == W - 1:
                if (case >> b - 1) & 1:
                    move[b][b - 1] += 1
                else:
                    move[b][b] += 1

            else:
                if (case >> b - 1) & 1:
                    move[b][b - 1] += 1
                elif (case >> b) & 1:
                    move[b][b + 1] += 1
                else:
                    move[b][b] += 1

    for h in range(1, H + 1):
        for w in range(W):
            for i in range(W):
                dp[h][w] += dp[h - 1][i] * move[i][w]

    print(dp[H][K - 1] % MOD)


def __starting_point():
    main()


__starting_point()
