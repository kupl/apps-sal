import math
import collections
from itertools import product

ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(map(int, input().split()))

n, k = mi()
h = [ii() for i in range(n)]
h.sort()
ans = 10**12
for i in range(n):
    last = i + k - 1
    if last >= n:
        break
    ans = min(ans, h[last] - h[i])
print(ans)
