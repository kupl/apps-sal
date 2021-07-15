n=int(input())
it=[input() for i in range(n)]
res,k=[],0
for i,x in enumerate(it):
    k=0
    for j,y in enumerate(x):
        if y=='.':
            res.append([i+1,j+1])
            k=1;break
    if k==0:break
if k==1:
    for i,x in enumerate(res):print(*x)
else:
    res,k=[],0
    for i,x in enumerate(it):
        k=0
        for j,y in enumerate(x):
            y=it[j][i]
            if y=='.':
                res.append([j+1,i+1])
                k=1;break
        if k==0:break
    if k==1:
        for i,x in enumerate(res):print(*x)
    else:print(-1)
