import sys
import numpy as np
(n, t) = map(int, input().split())
knapsack = np.zeros(t, dtype=np.int64)
cuisines = [tuple(map(int, line.split())) for line in sys.stdin]
cuisines.sort()
tmp_ans = 0
for (a, b) in cuisines:
    tmp_ans = max(tmp_ans, knapsack.max() + b)
    knapsack[a:] = np.maximum(knapsack[a:], knapsack[:-a] + b)
print(max(tmp_ans, knapsack.max()))
