n, m = list(map(int, input().split()))
num1 = n * (n -  1) // 2
if n % 2 == 0:
  num2 = (n // 2 + 1) * (n // 2) // 2 + \
         (n // 2 - 1) * (n // 2) // 2
else:
  num2 = (n // 2 + 1) * (n // 2)
s = 0
for _ in range(m):
  x, d = list(map(int, input().split()))
  s += x * n
  if d > 0:
    s += d * num1
  else:
    s += d * num2
print(s / n)

