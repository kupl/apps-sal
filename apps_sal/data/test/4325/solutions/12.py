n, x, t = map(int, input().split())

r1 = n // x
r2 = n % x

if r2 == 0:
  print(r1*t)
else:
  print((r1+1)*t)
