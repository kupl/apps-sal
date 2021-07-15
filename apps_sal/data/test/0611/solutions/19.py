n,m=list(map(int,input().split()))
ans=0
a=[]
for i in range(m):
    ip=list(map(int,input().split()))
    ans+=ip[0]
    a.append(ip[1])
ans*=n
pos=n*(n-1)//2
nn=n//2
neg=nn*(nn+1)
#print(ans,pos,neg)
if(n%2==0):
    neg-=nn
#print(ans,pos,neg)
for i in range(m):
    if(a[i]>0):
        ans+=a[i]*pos
    else:
        ans+=a[i]*neg
print(ans/n)
