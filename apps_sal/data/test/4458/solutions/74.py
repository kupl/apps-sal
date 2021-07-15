n=int(input())
l=list(map(int,input().split()))
a=n+1
ans=0
for i in range(n):
    if l[i]<=a:
        ans+=1
        a=l[i]
print(ans)
