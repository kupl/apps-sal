from itertools import accumulate
from operator import add, mul
n, m, q = map(int, input().split())

a = []
b = []
for i in range(n):
    a.append([0] * (n))
    b.append([0] * (n))

'''
for i in range(m):
    l,r=map(int,input().split())
    for j in range(r-1,n):
        for k in range(l):
            a[j][k]+=1
'''
for i in range(m):
    l, r = map(int, input().split())
    a[l - 1][r - 1] += 1


for i in range(n):
    a[i] = list(accumulate(a[i]))


for i in range(n):
    for j in range(n - i - 1):
        a[n - i - j - 2][n - i - 1] += a[n - i - j - 1][n - i - 1]


'''
for l in range(n):
    for r in range(l,n):
        temp=a[r][l]
        for i in range(r,n):
            for j in range(0,l+1):
                b[i][j]+=temp
'''

for i in range(q):
    P, Q = map(int, input().split())
    print(a[(P - 1)][(Q - 1)])
'''
for i in range(que):
    p,q=MI()
    if p==1:
        ans=lis[q-1][q-1]
    else:
        ans=lis[q-1][q-1]-lis[p-2][q-1]
    print(ans)
'''
