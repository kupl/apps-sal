# from itertools import combinations
# from bisect import bisect_left
# from functools import *
# from collections import Counter

def I(): return list(map(int, input().split()))


n, m = I()
ans = 0
columns = list(zip(*[input() for i in range(n)]))
g = [0 for _ in range(n)]
for column in columns:
    if sum(g[i] or column[i] <= column[i + 1] for i in range(n - 1)) == n - 1:
        for i in range(n - 1):
            g[i] |= column[i] < column[i + 1]
    else:
        ans += 1
print(ans)
