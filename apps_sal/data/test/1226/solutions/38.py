n, a, b = map(int,input().split())
mod = pow(10, 9) + 7
s, x, y = pow(2, n, mod) - 1, 1, 1
for i in range(1, b+1):
  x, y = x * (n-i+1) % mod, y * i % mod
  if i == a or i == b: s -= x * pow(y, mod - 2, mod)
print(s % mod)
