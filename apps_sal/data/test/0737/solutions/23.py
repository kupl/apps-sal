#!/usr/bin/env python3
# -*- coding: utf-8 -*-


n = int(input())
sq = int(n**(1 / 2))
ans = sq * 4
if n - sq**2 > sq:
    ans += 4
elif 1 <= n - sq**2 <= sq:
    ans += 2

print(ans)
