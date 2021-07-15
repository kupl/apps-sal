# -*- coding: utf-8 -*-
N, M = list(map(int, input().split(' ')))

a_b_pairs = [list(map(int, input().split(' '))) for _ in range(M)]
a_b_pairs.sort(key=lambda x: x[1])
right = a_b_pairs[0][1] - 1

ans = 1
for a, b in a_b_pairs[1:]:
    if a > right:
        right = b - 1
        ans += 1

print(ans)




