n=int(input())
w=list(map(int,input().split()))

ans=10**9
for t in range(1,n):
  ans=min(ans, abs(sum(w[:t])-sum(w[t:])))

print(ans)
