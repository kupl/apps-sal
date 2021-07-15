a, b = map(int, input().split())

ans = 0
if a >= b:
  for i in range(a):
    ans += b * 10**i
else:
  for i in range(b):
    ans += a * 10**i
print(ans)
