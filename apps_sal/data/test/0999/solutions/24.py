#!/bin/python3
arrn = []
arrm = []
maxstn = -1
minendn = 10**10
maxstm = -1
minendm = 10**10
n = int(input())
for i in range(n):
    arrn.append([int(x) for x in input().strip().split()])
    if arrn[i][0] > maxstn:
        maxstn = arrn[i][0]
    if arrn[i][1] < minendn:
        minendn = arrn[i][1]

m = int(input())
for i in range(m):
    arrm.append([int(x) for x in input().strip().split()])
    if arrm[i][0] > maxstm:
        maxstm = arrm[i][0]
    if arrm[i][1] < minendm:
        minendm = arrm[i][1]
ans = 0
if maxstn - minendm > ans:
    ans = maxstn - minendm
if maxstm - minendn > ans:
    ans = maxstm - minendn
print(ans)
