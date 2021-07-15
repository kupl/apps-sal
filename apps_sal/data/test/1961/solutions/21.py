#!/usr/bin/env python
    
n, m = [int(x) for x in input().split()]
mat = []
v = []

for i in range(n):
    mat.append([x == '#' for x in input()])
    v.append([False]*m)

def check(m, v, x, y):
    for i in (-1,0,1):
        for j in (-1,0,1):
            if (i,j) == (0,0):
                continue
            if not m[x+i][y+j]:
                return

    for i in (-1,0,1):
        for j in (-1,0,1):
            if (i,j) != (0,0):
                v[x+i][y+j] = True

for x in range(1, n-1):
    for y in range(1,m-1):
        check(mat, v, x, y)

flag = True
for i in range(0,n):
    for j in range(0,m):
        if mat[i][j] and (not v[i][j]):
            flag = False

if flag:
    print("YES")
else:
    print("NO")

