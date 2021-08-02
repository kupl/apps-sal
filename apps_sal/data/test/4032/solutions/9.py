# ===================================
# (c) MidAndFeed aka ASilentVoice
# ===================================
# import math
# import collections
# import string
# ===================================
n, k = [int(x) for x in input().split()]
q = [int(x) for x in input().split()]
l = 0
r = n - 1
ans = 0
while(l <= r and (q[l] <= k or q[r] <= k)):
    if l == r:
        ans += 1
        break
    if q[l] <= k:
        ans += 1
        l += 1
    if q[r] <= k:
        ans += 1
        r -= 1

print(ans)
