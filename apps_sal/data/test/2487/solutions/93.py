n=int(input())
ans=0
for i in range(n):
    ans+=(i+1)*(n-i)
for _ in range(n-1):
    a=list(map(int,input().split()))
    u=max(a)-1
    v=min(a)-1
    ans-=(v+1)*(n-u)
print(ans)
