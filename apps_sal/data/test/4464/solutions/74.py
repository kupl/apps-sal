# -*- coding: utf-8 -*-

A, B, C = map(int, input().split())

mod = []
for i in range(max(B, C)):
    res = A * i % B
    if res == C:
        ans = "YES"
        break
    if res in mod:
        ans = "NO"
        break
    mod.append(res)

print(ans)
