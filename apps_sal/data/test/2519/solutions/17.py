def e(n):
  return (int(n) + 1) / 2
n,k = map(int,input().split())
p = list(map(e,input().split()))
ans = sum(p[0:k])
temp = sum(p[0:k])
for i in range(1,n-k+1):
  temp += p[i+k-1] - p[i-1]
  ans = max(ans,temp)
print(ans)
