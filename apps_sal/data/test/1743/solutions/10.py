"""
Created on Fri Jan 18 12:23:03 2019

@author: nm57315
"""
n = int(input())
(a, b, c) = (list(map(int, input().strip().split())) for x in range(3))
(d, e) = (a[0], b[0])
for x in range(1, n):
    (d, e) = (max(e + a[x], d + b[x]), max(e + b[x], d + c[x]))
print(d)
