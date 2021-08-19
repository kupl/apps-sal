# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 00:39:17 2018

@author: shubham
"""


def Low(a, l, r, x):
    while l < r:
        mid = (l + r) // 2
        if a[mid] >= x:
            r = mid
        else:
            l = mid + 1
    if a[l] <= x:
        return l
    else:
        return l - 1


n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
k = list(map(int, input().split()))
p = [0] * n
p[0] = a[0]
for i in range(1, n):
    p[i] = p[i - 1] + a[i]
t = 0
for i in range(q):
    t += k[i]
    ans = Low(p, 0, n - 1, t)
    if ans == -1 or ans == n - 1:
        print(n)
    else:
        print(n - ans - 1)
    if ans == n - 1:
        t = 0
