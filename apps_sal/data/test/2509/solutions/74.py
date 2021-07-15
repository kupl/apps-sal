N, K = map(int, input().split())
ans = 0

for b in range(K+1, N+1):
  n = b - K
  t = N // b
  r = N % b
  ans += n*t + max(0, r - max(K-1, 0))

print(ans)
