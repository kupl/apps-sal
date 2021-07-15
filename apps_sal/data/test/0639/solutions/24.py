n,k=map(int,input().split())
l=list(map(int,input().split()))
ans=0
l.sort()
for i in range(n):
    if l[i]<k:
        ans+=1
print(k-ans+int(k in l))
