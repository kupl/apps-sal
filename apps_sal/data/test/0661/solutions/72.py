m,k=map(int,input().split())
if 1<<m<=k:print(-1);return()
if m==1:print(*[-1]if k else [0,0,1,1]);return
l=[i for i in range(1<<m)if i!=k]
print(*(l+[k]+l[::-1]+[k]))
