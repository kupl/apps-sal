n=int(input())
a=list(map(int,input().split()))
a=sorted(a)
b=list(set(a))
m=len(b)

p=[0]*(10**6+1)
for i in b:
    if p[i]==0:
        j=2
        while i*j<=10**6:
            p[i*j]=1
            j+=1
a.append(-1)
a.insert(0,-1)
ans=0
for i in range(1,n+1):
    if a[i]!=a[i+1] and a[i]!=a[i-1] and p[a[i]]==0:
        ans+=1
print(ans)

