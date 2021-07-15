n,a,b = list(map(int,input().split()))
ans = n // (a+b) * a
n %= (a+b)
if n > a:
  print(ans + a)
else:
  print(ans + n)
