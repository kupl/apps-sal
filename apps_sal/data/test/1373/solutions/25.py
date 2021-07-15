N, K = map(int, input().split())
big = 10**9+7
ans = 0
def sum2(begin,end):
  return (begin+end)*(end-begin+1)//2
for k in range(K,N+2):
  ans += (sum2(N+1-k+1,N+1)-sum2(1,k)+1)%big
print(ans%big)
