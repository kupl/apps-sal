#import math
#import collections
n, k = map(int, input().split())
#A = list(map(int, input().split( )))
mod = 10**9 + 7
ans = 0
l, h = 0, 0
for x in range(1, n + 2):
    l += x - 1
    h += n - x + 1
    if x >= k:
        ans += (h - l + 1)
        ans = ans % mod
print(ans)
