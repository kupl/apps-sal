n,x,m=map(int,input().split())

check=[0]*(m+1)
tmp=x%m
al=[x%m]
check[x%m]=1
while(True):
    tmp=tmp*tmp%m
    al.append(tmp)
    if check[tmp]==0:
        check[tmp]=1
    else:
        break
j=[]
start=0
flag=False
for i in range(len(al)):
    if al[i]==al[-1] and i!=len(al)-1:
        flag=True
        start=i
    if flag:
        if i!=len(al)-1:
            j.append(al[i])

ans=0
for i in range(start):
    ans+=al[i]

p=n-start
ans+=sum(j)*(p//len(j))
y=p%len(j)
for i in range(y):
    ans+=j[i]

print(ans)
