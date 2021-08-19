import sys
import itertools
import pprint


def input():
    return sys.stdin.readline().rstrip()


(H, W, K) = list(map(int, input().split()))
S = [[0 for _ in range(W)] for _ in range(H)]
for i in range(H):
    S[i] = list(map(int, input()))
Stsum = [[0 for _ in range(W + 1)] for _ in range(H + 1)]
for i in range(H):
    for j in range(W):
        Stsum[i + 1][j + 1] = Stsum[i + 1][j] + S[i][j]
for j in range(W):
    for i in range(H):
        Stsum[i + 1][j + 1] += Stsum[i][j + 1]


def count_white(l, r, u, b):
    return Stsum[b][r] - Stsum[u][r] - Stsum[b][l] + Stsum[u][l]


def solve():
    comb = list(itertools.product(list(range(2)), repeat=H - 1))
    ans = 10 ** 9 + 7
    for c in comb:
        hc = [0] + [i + 1 for (i, x) in enumerate(c) if x == 1] + [H]
        (l, w) = (0, 1)
        cut_count = 0
        search = False
        p_cut = True
        while w <= W:
            cut = True
            for h in range(0, len(hc) - 1):
                if count_white(l, w, hc[h], hc[h + 1]) > K:
                    cut = False
                    break
            else:
                search = True
            if not cut:
                if search:
                    l = w - 1
                    cut_count += 1
                    search = False
                else:
                    p_cut = False
                    break
            else:
                w += 1
        if p_cut:
            ans = min(ans, cut_count + len(hc) - 2)
    print(ans)


def __starting_point():
    solve()


__starting_point()
