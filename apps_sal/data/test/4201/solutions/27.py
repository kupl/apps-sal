"""
Created on Sun Sep  6 01:25:38 2020

@author: liang
"""

from itertools import combinations

H, W, K = map(int, input().split())

C = [input() for _ in range(H)]

ans = 0
for comb_H in [list(combinations(range(H), a)) for a in range(H + 1)]:
    for comb_W in [list(combinations(range(W), a)) for a in range(W + 1)]:
        for tuple_H in comb_H:
            for tuple_W in comb_W:
                tmp = 0
                for i in range(H):
                    for j in range(W):
                        if i not in tuple_H and j not in tuple_W and C[i][j] == "
                        tmp += 1
                if tmp == K:
                    ans += 1
print(ans)
