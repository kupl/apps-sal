n,m = [int(x) for x in input().split()]

A = []

B = []

for _ in range(n):
    A.append([int(x) for x in input().split()])

for _ in range(n):
    B.append([int(x) for x in input().split()])

AD = []
BD = []
for s in range(2,m+n+1):
    at = []
    bt = []
    for r in range(1,n+1):
        c = s-r
        if 1 <= c and c <= m:
            at.append(A[r-1][c-1])
            bt.append(B[r-1][c-1])
    at.sort()
    bt.sort()
    AD.append(at)
    BD.append(bt)
    
if AD == BD:
    print('YES')

else:
    print('NO')
