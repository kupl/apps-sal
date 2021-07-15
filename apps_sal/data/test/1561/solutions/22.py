y,x,k=map(int,input().split())
m=[];ans=0
for i in range(y):
    m.append(list(input()))
    e=0
    for z in m[i]:
        if z=='.':
            e+=1
        else:
            ans+=max(0,e-k+1)
            e=0
    ans+=max(0,e-k+1)
if k-1:
    for j in range(x):
        e=0
        for i in range(y):
            if m[i][j]=='.':
                e+=1
            else:
                ans+=max(0,e-k+1)
                e=0
        ans+=max(0,e-k+1)
print(ans)
