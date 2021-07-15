def ncr(n, r):
  if n < r:
    return 0
  res = 1
  for i in range(1, n + 1):
    res *= i
  for i in range(1, r + 1):
    res //= i
  for i in range(1, n - r + 1):
    res //= i
  return res
n, a, b = list(map(int, input().split()))
v = sorted(list(map(int, input().split())), reverse=True)
print((sum(v[0:a]) / a))
if v[0] == v[a - 1]:
  c = v.count(v[0])
  ans = 0
  for i in range(a, b + 1):
    ans += ncr(c, i)
  print(ans)
else:
  k = v.count(v[a - 1])
  r = v[0:a].count(v[a - 1])
  print((ncr(k, r)))

