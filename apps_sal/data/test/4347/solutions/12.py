n=int(input())
ans=1
for i in range(1,n+1):
    ans=ans*i
ans=ans//(n//2)
ans=ans//(n//2)
ans=ans//2
print(ans)
