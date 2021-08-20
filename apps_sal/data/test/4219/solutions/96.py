import sys
input = sys.stdin.readline
'\na,b=[],[]\nfor i in range(n):\n    A, B = map(int, input().split())\n    a.append(A)   \n    b.append(B)'
n = int(input())
(a, x) = ([], [])
for i in range(n):
    A = int(input())
    a.append(A)
    B = []
    for j in range(A):
        B.append(list(map(int, input().split())))
    x.append(B)
ma = 0
for i in range(2 ** n):
    now = 0
    flg = True
    e = [0] * n
    for j in range(n):
        if i >> j & 1:
            now += 1
            e[j] = 1
    for j in range(n):
        if i >> j & 1:
            if e[j] == 0:
                flg = False
                break
            elif not flg:
                break
            for k in range(a[j]):
                'if e[x[j][k][0]-1]==-1: \n                    if x[j][k][1] and\n                    e[x[j][k][0]-1]=x[j][k][1]'
                if e[x[j][k][0] - 1] == 0 and x[j][k][1] == 1 or (e[x[j][k][0] - 1] == 1 and x[j][k][1] == 0):
                    flg = False
                    break
    if flg and ma < now:
        ma = now
print(ma)
