W,H,N=map(int, input().split())
X=[0,W]
Y=[0,H]

for i in range(N):
    x,y,a = map(int, input().split())
    if a==1:
        X[0]=max(x, X[0])
    elif a==2:
        X[1]=min(x, X[1])
    elif a==3:
        Y[0]=max(y, Y[0])
    else:
        Y[1]=min(y, Y[1])

if X[1]-X[0]<=0 or Y[1]-Y[0]<=0:
    area=0
else:
    area = max(0,(X[1]-X[0])*(Y[1]-Y[0]))
print(area)
