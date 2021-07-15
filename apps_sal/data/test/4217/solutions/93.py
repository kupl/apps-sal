import numpy as np
n,m = map(int,input().split())
k = np.zeros(n,dtype=int)
a = np.zeros((n,m),dtype=int)
for i in range(n):
    p = list(map(int, input().split()))
    k[i] = p[0]
    for j in range(1,len(p)):
        a[i][j-1] = p[j]
ans = np.zeros(n+m,dtype=int)
for i in range(n):
    for j in range(m):
        if a[i][j] != 0:
            s = a[i][j]-1
            ans[s] += 1
an = 0
for i in range(n+m):
    if ans[i] == n:
        an += 1
print(an)
