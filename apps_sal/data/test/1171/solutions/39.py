#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 問題：https://atcoder.jp/contests/abc128/tasks/abc128_d

n, k = list(map(int, input().strip().split()))
value = list(map(int, input().strip().split()))
res = 0
for l in range(k + 1):
    for r in range(k - l + 1):
        if l + r > n:
            continue
        d = k - l - r
        now = 0
        s = []
        for i in range(l):
            now += value[i]
            s.append(value[i])
        for i in range(r):
            now += value[n - i - 1]
            s.append(value[n - i - 1])
        s.sort()
        for i in range(d):
            if i >= len(s):
                break
            if s[i] > 0:
                break
            now -= s[i]
        res = max(res, now)

print(res)
