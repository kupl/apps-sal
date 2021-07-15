n,m=map(int,input().split())
x=[]
y=[]
cnt=0
for i in range(0,min(n,m)+1):
    cnt+=1
    x.append(i)
    y.append(min(n,m)-i)
print(cnt)
for i in range(cnt):
    print(x[i],y[i])
