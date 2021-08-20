"""
References: <https://www.hamayanhamayan.com/entry/2020/03/22/231629>
"""
import sys
from itertools import product
input = sys.stdin.readline


def main():
    (H, W, K) = list(map(int, input().split()))
    S = [None] * H
    for i in range(H):
        S[i] = input().rstrip()
    ans = float('inf')
    for comb in product(list(range(2)), repeat=H - 1):
        n_cut = sum(comb)
        if n_cut >= ans:
            continue
        group = []
        g_id = 0
        for c in comb:
            group.append(g_id)
            if c == 1:
                g_id += 1
        group.append(g_id)
        w = 0
        while w < W:
            count = [0] * (g_id + 1)
            next_w = w
            for x in range(w, W):
                over_K = False
                for y in range(H):
                    if S[y][x] == '1':
                        count[group[y]] += 1
                        if count[group[y]] > K:
                            over_K = True
                            break
                if over_K:
                    break
                next_w += 1
            if next_w == w:
                n_cut = float('inf')
                break
            w = next_w
            if over_K:
                n_cut += 1
            if n_cut >= ans:
                break
        if n_cut < ans:
            ans = n_cut
    print(ans)


def __starting_point():
    main()


__starting_point()
