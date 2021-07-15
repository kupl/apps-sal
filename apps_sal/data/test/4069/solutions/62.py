x, k, d = map(int, input().split())
x = abs(x)
if x > k * d:
  ans = x - k * d
else:
  a = x // d
  b = x % d
  k -= a
  if k % 2 == 0:
    ans = b
  else:
    ans = abs(b-d)
print(ans)
