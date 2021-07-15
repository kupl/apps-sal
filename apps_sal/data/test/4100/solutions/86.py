import sys

n,k,q=list(map(int,input().split()))
a=[int(input()) for i in range(q)]

if k>q:
    for i in range(n):
        print('Yes')
    return

d=[0]*n

for i in range(q):
    d[a[i]-1]=d[a[i]-1]+1

for j in d:
    if j>q-k:
        print('Yes')
    else:
        print('No')

