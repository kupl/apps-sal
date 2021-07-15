n,ma,mb=list(map(int,input().split()))
el=[list(map(int,input().split())) for i in range(n)]
sa=sum(i[0] for i in el)
sb=sum(i[1] for i in el)
sa1=sa+1
sb1=sb+1

inf=1000000
x=[[inf]*(sb1) for i in range(sa1)]
x[0][0]=0
for i in range(n):
    now=el[i]
    x_sub=[[0]*(sb1) for i in range(sa1)]
    for k in range(sa1):
        for l in range(sb1):
            if x[k][l]!=inf:
                if k+now[0]<sa1:
                    if l+now[1]<sb1:
                        x_sub[k+now[0]][l+now[1]]=x[k][l]+now[2]
    for k in range(sa1):
        for l in range(sb1):
                if x_sub[k][l]!=0:
                    x[k][l]=min(x[k][l],x_sub[k][l])
mi=min(sa//ma,sb//mb)
ans=inf
for i in range(1,mi+1):
    ans=min(ans,x[ma*i][mb*i])
if ans==inf:
    print((-1))
else:
    print(ans)

