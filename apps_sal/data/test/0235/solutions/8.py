def f(n, k):
  m = n
  p, v = 0, 0
  while n > 0:
    p += min(k, n)
    n -= min(n, k)
    if p >= m // 2:
      break
    v += n // 10
    n -= n // 10
    if v > m // 2:
      break
  return p >= v

n = int(input())

l, u = 1, n
while (l != u):
  m = (l + u) // 2
  if not f(n, l) and not f(n, m):
    l = m + 1
  elif f(n, m) and f(n, u):
    u = m
print(l)

