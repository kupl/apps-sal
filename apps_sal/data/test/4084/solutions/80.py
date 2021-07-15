n,a,b = map(int, input().split())
ans = 0
x = n // (a+b)
y = n % (a+b)
if y < a:
  print(x*a + y)
else:
  print(x*a + a)
