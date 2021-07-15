n = int(input())
a = list(map(int, input().split()))
s = sum(a)
k = 0
if n > 3 and s % 3 == 0:
  s //= 3
  c = [0] * n
  t = 0
  for i in range(n):
    t += a[n - i - 1]
    if t == s:
      c[n - i - 1] = 1
  for i in range(n - 1):
    c[n - i - 2] += c[n - i - 1]
  t = 0
  for i in range(n - 2):
    t += a[i]
    if t == s:
      k += c[i + 2]
print(k)
