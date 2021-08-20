from itertools import accumulate
from operator import add, mul
(n, m, q) = map(int, input().split())
a = []
b = []
for i in range(n):
    a.append([0] * n)
    b.append([0] * n)
'\nfor i in range(m):\n    l,r=map(int,input().split())\n    #print(a[(r-1):n,0:l])\n    #a[(r-1):n,0:l]+=1\n    for j in range(r-1,n):\n        for k in range(l):\n            a[j][k]+=1\n'
for i in range(m):
    (l, r) = map(int, input().split())
    a[l - 1][r - 1] += 1
for i in range(n):
    a[i] = list(accumulate(a[i]))
for i in range(n):
    for j in range(n - i - 1):
        a[n - i - j - 2][n - i - 1] += a[n - i - j - 1][n - i - 1]
'\nfor l in range(n):\n    for r in range(l,n):\n        temp=a[r][l]\n        for i in range(r,n):\n            for j in range(0,l+1):\n                b[i][j]+=temp\n        #b[r:n,0:l+1]+=temp\n'
for i in range(q):
    (P, Q) = map(int, input().split())
    print(a[P - 1][Q - 1])
'\nfor i in range(que):\n    p,q=MI()\n    if p==1:\n        ans=lis[q-1][q-1]\n    else:\n        ans=lis[q-1][q-1]-lis[p-2][q-1]\n    print(ans)\n'
