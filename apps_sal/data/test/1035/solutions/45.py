import math

a,b = map(int, input().split())
t = math.gcd(a,b)

def prime_decomposition(n):
  i = 2
  table = []
  while i * i <= n:
    while n % i == 0:
      n /= i
      table.append(i)
    i += 1
  if n > 1:
    table.append(n)
  return table

cnt = len(set(prime_decomposition(t)))

print(cnt+1)
