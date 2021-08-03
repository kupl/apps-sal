# -*- coding: utf-8 -*-
# get a integer
N = int(input())
# get two integers separated with half-width break
L = list(map(int, input().split()))
# get a string

# output"
L.sort()
L = L[::-1]

r = 0
for i in range(N):
    r += L[1]
    L = L[2:]

print((str(r)))
