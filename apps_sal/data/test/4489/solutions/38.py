#!/usr/bin/env python3
from collections import Counter

n = int(input())
s = [str(input()) for i in range(n)]
m = int(input())
t = [str(input()) for i in range(m)]

s = Counter(s)

t = Counter(t)

ans = 0
for i in list(s.keys()):
    if i in t:
        ans_tmp = s[i] - t[i]
    else:
        ans_tmp = s[i]
    ans = max(ans, ans_tmp)
print(ans)
