n, k = map(int,input().split())
a = list(map(int,input().split()))
b = [[] for i in range(0,k+1)]
u = [0]*(n*k+1)
for i in range(k):
    b[i].append(a[i])
    u[a[i]]=1
p = 0;
for i in range (1,n*k+1):
    if u[i]==0:
        u[i]=1
        b[p].append(i)
    if len(b[p]) == n:
        p += 1
for i in range(k):
    for j in range(n):
        print(b[i][j],end=' ')
    print()

