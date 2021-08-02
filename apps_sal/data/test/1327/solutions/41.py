#!/usr/bin/env python3
from itertools import product
n, m = list(map(int, input().split()))
xyz = [list(map(int, input().split())) for i in range(n)]

dp = [[0 for i in range(m + 1)] for j in range(n + 1)]


# eval
# eval_list = ["+xyz[i-1][0]+xyz[i-1][1]+xyz[i-1][2]",
#              "+xyz[i-1][0]+xyz[i-1][1]-xyz[i-1][2]",
#              "+xyz[i-1][0]-xyz[i-1][1]+xyz[i-1][2]",
#              "+xyz[i-1][0]-xyz[i-1][1]-xyz[i-1][2]",
#              "-xyz[i-1][0]+xyz[i-1][1]+xyz[i-1][2]",
#              "-xyz[i-1][0]+xyz[i-1][1]-xyz[i-1][2]",
#              "-xyz[i-1][0]-xyz[i-1][1]+xyz[i-1][2]",
#              "-xyz[i-1][0]-xyz[i-1][1]-xyz[i-1][2]", ]

ans = 0
for a, b, c in product([1, -1], repeat=3):
    total = []
    for x, y, z in xyz:
        s = x * a + y * b + z * c
        total.append(s)
    total.sort(reverse=True)
    ans = max(ans, sum(total[:m]))
print(ans)
