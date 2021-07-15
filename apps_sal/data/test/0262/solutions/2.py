#!/usr/bin/env python3

n = int(input())
s = [[int(x) for x in input().split()] for _ in range(n)]

p, q = 0, 0

for i in range(n):
    for j in range(n):
        if s[i][j] == 0:
            p, q = i, j

if n > 1:
    m = sum(s[(p+1)%n])
    s[p][q] = m - sum(s[p])
else:
    m = 1
    s[p][q] = 1

f = True

for i in range(n):
    if sum(s[i]) != m:
        f = False
    if sum(s[j][i] for j in range(n)) != m:
        f = False
        
if sum(s[i][i] for i in range(n)) != m:
    f = False
if sum(s[i][n-i-1] for i in range(n)) != m:
    f = False

if f and s[p][q] > 0:
    print(s[p][q])
else:
    print("-1")

