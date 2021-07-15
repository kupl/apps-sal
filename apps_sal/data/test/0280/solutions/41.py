from bisect import bisect_left
from collections import namedtuple
from itertools import permutations

n,m = map(int,input().split())
w = list(map(int,input().split()))
P = [tuple(map(int,input().split())) for _ in range(m)]
P.sort(key = lambda x:x[1])
ls = [p[0] for p in P]
vs = [p[1] for p in P]
for i in range(1,m):
    ls[i] = max(ls[i-1],ls[i])

if max(w)>min(vs):
    print(-1);return

ans = float('inf')
for ws in permutations((w)):
    pref = [ws[0]]
    for i in range(1,n):
        pref.append(pref[i-1]+ws[i])
    dp = [0]*n
    for i in range(n):
        for j in range(i):
            interval = pref[i]-(pref[j-1] if j>=1 else 0)
            idx = bisect_left(vs,interval)
            need = ls[idx-1] if idx>=1 else 0
            dp[i] = max(dp[i],dp[j]+need)
    ans = min(ans,dp[-1])
print(ans)
