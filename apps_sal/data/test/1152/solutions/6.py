from collections import defaultdict
(n, m) = [int(i) for i in input().split()]
A = []
for i in range(n):
    B = [int(j) for j in input().split()]
    A.append(B)
B = []
for i in range(n):
    C = [int(j) for j in input().split()]
    B.append(C)
changesx = []
changesy = []
for i in range(n):
    for j in range(m):
        if A[i][j] != B[i][j]:
            changesx.append(i)
            changesy.append(j)
ddx = defaultdict(int)
ddy = defaultdict(int)
for i in changesx:
    ddx[i] += 1
for i in changesy:
    ddy[i] += 1
ok = 1
for i in ddx:
    if ddx[i] % 2 != 0:
        ok = 0
for i in ddy:
    if ddy[i] % 2 != 0:
        ok = 0
if ok:
    print('Yes')
else:
    print('No')
