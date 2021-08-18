
"""
"""

from operator import itemgetter

n, v = list(map(int, input().split()))

if v >= n - 1:
    ans = n - 1
else:
    ans = v + ((2 + (2 + n - v - 2)) * (n - v - 1)) // 2
print(ans)
