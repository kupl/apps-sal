n,k=map(int,input().split())
num=k
ans=1
while num-1<n:
    ans+=1
    num*=k
print(ans)
