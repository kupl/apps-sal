n=int(input())
ans=0
for i in range(1,n):
    if n%i==0:
        ans+=n//i -1
    else:
        ans+=n//i

print(ans)
