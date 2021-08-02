# -*- coding: utf-8 -*-

n, d = list(map(int, input().split()))
a = list(map(int, input().split()))
m = int(input())

a.sort()
if m <= n:
    print(sum(a[:m]))
else:
    print(sum(a) - (m - n) * d)
