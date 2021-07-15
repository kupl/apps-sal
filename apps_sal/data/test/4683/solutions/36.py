N = int(input())
mod = 10**9 + 7
A = list(map(int, input().split()))
Asum = sum(A)
ans = 0
for a in A:
  Asum -= a
  ans += a*Asum % mod
print(ans % mod)
