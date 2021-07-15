n,k=list(map(int,input().split()))
d=list(map(int,input().split()))
nd=list(map(int,input().split()))
diff=[]
for i in range(n):
    diff.append((d[i]-nd[i], i))
ans=0
diff=sorted(diff, key=lambda x:x[0])
for i in range(k):
    temp,ind=diff[i]
    ans+=d[ind]
for i in range(k,n):
    temp,ind=diff[i]
    if temp<0:
        ans+=d[ind]
    else:
        ans+=nd[ind]
print(ans)

