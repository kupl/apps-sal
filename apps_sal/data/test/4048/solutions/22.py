n=int(input())
k = 1
ans = n - 1
while k*k <= n:
  if n % k == 0:
    r = n // k
    ans = min(ans, k + r - 2)
  k += 1
print(ans)
