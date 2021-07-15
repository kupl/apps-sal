N, K = map(int, input().split())

mod = 10 ** 9 + 7
ans = 0

for i in range(K, N+2):
  ans += ((N + 1) * i - i ** 2 + 1) % mod
  
print(ans % mod)
