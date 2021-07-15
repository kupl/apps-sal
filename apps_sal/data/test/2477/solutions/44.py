import sys

n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

l, r = 0, max(a)
while r - l > 1:
  # satisfy l < t < r
  t = (l + r) // 2
  c = sum([(e-1) // t for e in a])
  if k < c:
    l = t
  else:
    r = t
print(r)
