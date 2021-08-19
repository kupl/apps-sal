from itertools import groupby
import math
(n,) = list(map(int, input().strip().split()))
array = list(map(int, input().strip().split()))
g_array = [k for (k, g) in groupby(array)]
n = len(g_array)
extend_n = n + 2
sols = [[0] * extend_n for _ in range(extend_n)]
for i in range(1, extend_n - 1):
    for j in range(extend_n - 2, i, -1):
        val = max(sols[i - 1][j], sols[i][j + 1])
        if g_array[i - 1] == g_array[j - 1]:
            val = max(val, sols[i - 1][j + 1] + 1)
        sols[i][j] = val
best = 0
for start in range(1, extend_n - 1 - 1):
    start_val = sols[start - 1][start + 1]
    if start_val > best:
        best = start_val
print(len(g_array) - 1 - best)
