N, K = map(int,input().split())
ans = 0
while K <= N+1:
  ans += ((N+1)*(N+2) - (N-K+1)*(N-K+2) - K*(K+1)) // 2 + 1
  K += 1
print(ans % (10 ** 9 + 7))
