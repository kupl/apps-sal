n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
for i in a:
  n -= i
  if n < 0:
    break
if n < 0:
  print((-1))
else:
  print(n)

