# ===================================
# (c) MidAndFeed aka ASilentVoice
# ===================================
# import math, fractions, collections
# ===================================
n, m = [int(x) for x in input().split()]
q = [int(x) for x in input().split()]
ans = 1e9
for i in range(1, n + 1):
    s = q.count(i)
    ans = min(ans, s)
print(ans)
