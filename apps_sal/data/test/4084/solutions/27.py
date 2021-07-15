n, a, b = map(int, input().split())

c = n//(a+b)
ans = c*a
n = n - c*(a+b)
if n < a:
  print(ans + n)
else:
  print(ans + a)
