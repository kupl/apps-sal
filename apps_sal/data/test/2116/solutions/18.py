# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 21:02:31 2016

@author: Kirill
"""

n, m, k = map(int, input().split())
order = list(map(int, input().split()))
items = []
for i in range(n):
    items.append(list(map(int, input().split())))

ans = 0
for i in range(n):
    for j in range(m):
        item = order.index(items[i][j])
        ans += item + 1
        order.insert(0, order.pop(item))
print(ans)
