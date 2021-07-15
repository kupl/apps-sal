n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
lis=[]
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
ans=0        
for i in d:
    if d[i]>1:
        lis.append(i)
for i in range(len(lis)):
    for j in range(n):
        if lis[i]==a[j]:
            ans+=b[j]            
for i in range(n):
    if d[a[i]]==1:
        c=0
        for j in range(len(lis)):
            if a[i]&lis[j]==a[i]:
                lis.append(a[i])
                ans+=b[i]
                break
print(ans)            
