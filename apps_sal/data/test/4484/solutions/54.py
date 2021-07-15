n, m = map(int, input().split())
n, m = max(n, m), min(n, m)
div = 10 ** 9 + 7
res = 1
if n - m == 0:
  for i in range(1, n + 1):
    res *= i
    res %= div
  res = res * res * 2
  print(res % div)
elif n - m == 1:
  for i in range(1, n + 1):
    res *= i
    res %= div
  for i in range(1, m + 1):
    res *= i
    res %= div
  print(res)
else:
  print(0)
