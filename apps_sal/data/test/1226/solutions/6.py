#フェルマーの小定理
#繰り返し2乗法

n, a, b = map(int,input().split())
mod = pow(10, 9) + 7
s = pow(2, n, mod) - 1
x = 1
y = 1
for i in range(1, b+1):
  x = x * (n-i+1) % mod
  y = y * i % mod
  if i == a or i == b:
    s -= x * pow(y, mod - 2, mod)

print(s % mod)
