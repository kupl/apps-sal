N,K = list(map(int, input().split()))

ans = 0

for b in range(1,N+1):
  if b<=K:
    continue
  ans += (N//b) * (b-K)
  ans += max(N%b-K+1, 0)
  if K == 0:
    ans -= 1
print(ans)

