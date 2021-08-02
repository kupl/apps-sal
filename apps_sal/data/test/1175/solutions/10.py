import sys
import math

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def main():
    md = 10 ** 9 + 7
    l, r = list(map(int, input().split()))
    n = int(math.log2(r)) + 1
    # dp[i][t][f][g] i桁目まで見て最上位が決定済みか(t)、L<xが確定(f)、y<Rが確定
    dp = [[[[0] * 2 for _ in range(2)] for __ in range(2)] for ___ in range(n + 1)]
    dp[0][0][0][0] = 1
    ans = 0
    for i in range(n):
        lk = l >> (n - 1 - i) & 1
        rk = r >> (n - 1 - i) & 1
        for t in range(2):
            for f in range(2):
                for g in range(2):
                    pre = dp[i][t][f][g]
                    for x, y in [(0, 0), (0, 1), (1, 1)]:
                        nt, nf, ng = t, f, g
                        if t == 0 and (x, y) == (0, 1): continue
                        if f == 0 and lk > x: continue
                        if g == 0 and y > rk: continue
                        if (x, y) == (1, 1): nt = 1
                        if lk == 0 and x == 1: nf = 1
                        if y == 0 and rk == 1: ng = 1
                        if i == n - 1:
                            ans = (ans + pre) % md
                        else:
                            dp[i + 1][nt][nf][ng] = (dp[i + 1][nt][nf][ng] + pre) % md
    print(ans)


main()
