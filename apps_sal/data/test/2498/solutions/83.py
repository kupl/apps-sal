import math

def lcm(a, b):
  return a*b//math.gcd(a, b)

def f(num):
  cnt = 0
  while num % 2 == 0:
    num = num // 2
    cnt += 1
  return cnt

n, m = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
  a[i] = a[i] // 2

t = f(a[0])
for i in range(n):
  if f(a[i]) != t:
    print(0)
    return
  a[i] = a[i] >> t
m = m >> t
l = 1
for i in range(n):
  l = lcm(l, a[i])
  if l > m:
    print(0)
    return

m = m // l
print((m+1)//2)
