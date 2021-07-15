N = int(input())
K = int(input())

ans = float("inf")
for i in range(N+1):
  num = 1 * (2 ** i) + K * (N - i)
  ans = min(ans, num)
  
print(ans)
