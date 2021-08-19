#!/usr/bin/env python

n, m = list(map(int, input().split()))

cc = m // 2
ans = min(n, cc)
res = cc - min(n, cc)
if res > 0:
    ans += res // 2
print(ans)
