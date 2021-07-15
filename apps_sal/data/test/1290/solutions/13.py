n,m=list(map(int,input().split()))
pts=[0 for i in range(n)]
a=list(map(int,input().split()))
for i in range(m):
    x=a[i]-1
    pts[x]+=1
print(min(pts))





