m,n=map(int, input().split())
a=[0]*8
for i in range(m):
    x=list(map(int, input().split()))
    for j in range(1, n+1):
        a[j]=max(a[j], a[j-1])+x[j-1]
    print(a[n], end=' ') 
