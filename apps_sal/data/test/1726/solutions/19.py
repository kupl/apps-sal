n,t=map(int,input().split())
a=list(map(int,input().split()))
ans=0
total=0
for i in range(n):
    total+=86400-a[i]
    ans+=1
    if total>=t:
        break
print(ans)
