N, K = map(int, input().split())
ans = 0
if K == 0:
  print(N**2)
  return
for b in range(K+1, N+1):
  #print(b)
  #print(N // b * (b - K), max((N%b)-(K-1), 0))
  ans += N // b * (b - K)
  ans += max((N%b)-(K-1), 0)
print(ans)
