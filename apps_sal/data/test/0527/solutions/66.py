#!/usr/bin/env python3
from bisect import bisect_right

s = input()
N = len(s)
si = [[] for _ in range(26)]
for i in range(N):
    si[ord(s[i]) - ord('a')].append(i + 1)

ans = 0
t = input()
M = len(t)
for j in range(M):
    ti = si[ord(t[j]) - ord('a')]
    if len(ti) == 0:
        print(-1)
        return
    d = bisect_right(ti, ans % N)
    if d == len(ti):
        ans += ti[0] + N - ans % N
    else:
        ans += ti[d] - ans % N
print(ans)
