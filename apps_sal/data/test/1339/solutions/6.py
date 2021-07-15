def Q(x):
    return x[1]-x[0]+1
n=int(input())
L=[]
for i in range(n):
    x,y=list(map(int,input().split()))
    L.append((x,y,i+1))

L.sort(key=Q,reverse=True)
ans=L[0][2]
for i in range(1,n):
    if(L[i][0]>=L[0][0] and L[i][1]<=L[0][1]):
        continue
    ans=-1
print(ans)

