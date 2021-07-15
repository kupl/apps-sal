n = int(input())
w = list(map(int,input().split()))
ans = abs(w[0] - sum(w[1:]))
for i in range(1,n-1):
  ans = min(ans,abs(sum(w[:i+1])-sum(w[i+1:])))
print(ans)
