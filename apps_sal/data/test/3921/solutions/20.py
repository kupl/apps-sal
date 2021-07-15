n=int(input())
x=list(map(int,input().split()))
v=[[] for i in range(100001)]
max,ans=[0]*100001,0
for i2 in range(1,x[n-1]+1):
    for i in range(i2,x[n-1]+1,i2):
        v[i].append(i2)
for i in range(n):
    temp=0
    for i2 in range(1,len(v[x[i]])):
        if temp<max[v[x[i]][i2]]:
            temp=max[v[x[i]][i2]]
    temp+=1
    for i2 in range(1,len(v[x[i]])):
        if temp>max[v[x[i]][i2]]:
            max[v[x[i]][i2]]=temp
    if ans<temp:
        ans=temp
print(ans)
