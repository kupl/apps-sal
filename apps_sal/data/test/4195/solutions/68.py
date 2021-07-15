d,n = list(map(int, input().split()))

if d == 0:
  if n == 100:
    ans = 101
  else:
    ans = n
elif d == 1:
  if n == 100:
    ans = 10100
  else:
    ans = n * 100
elif d == 2:
  if n == 100:
    ans = 1010000
  else:
    ans = n * 10000
print(ans)
