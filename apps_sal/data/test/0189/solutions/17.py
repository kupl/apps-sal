import math
n = int(input())
ar = [*map(int, input().split(' '))]
(mint, mincost) = (int(1000000000.0), int(1000000000.0))
for i in range(1, 105):
    cost = sum([min(abs(x - i), abs(x - i - 1), abs(x - i + 1)) for x in ar])
    if cost < mincost:
        mincost = cost
        mint = i
print(int(mint), int(mincost))
