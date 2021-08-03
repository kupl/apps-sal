# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 01:24:22 2020

@author: liang
"""

MOD = 10**9 + 7
N = int(input())
data = [i for i in range(2, N + 1)]
table = list()

# 素数リスト
while data:
    tmp = data[0]
    table.append(tmp)
    data = [i for i in data if i % tmp != 0]

# print(table)
res = dict()
for i in range(2, N + 1):
    for t in table:
        if i % t == 0:
            if t not in res:
                res[t] = 1
            tmp = i
            while tmp % t == 0:
                res[t] += 1
                tmp //= t

ans = 1
for r in res.values():
    ans *= r
    ans %= MOD
# print(res)
print(ans)
