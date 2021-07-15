N = int(input())
A = list(map(int, input().split()))

MOD = 10**9 + 7
s = 0

for i in range(N):
  s += A[i]
ans = 0
for i in range(N-1):
  s -= A[i]
  ans += A[i] * s
  ans %= MOD

print(ans)
