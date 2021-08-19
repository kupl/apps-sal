# -*- coding: utf-8 -*-
n = int(input())
alist = list(map(int, input().split()))
ans = 0
b = 0
c = 0
k = 0
for i in range(n):
    b += alist[i]
    c += alist[0 + k]
    if b < c:
        ans += c - b
        b = c
    elif b > c:
        k = i
        c = b
print(ans)
