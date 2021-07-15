n = int(input())
ans = float(0)
for _ in range(n):
  m, u = input().split()
  m = float(m)
  if u == 'JPY':
    ans += m
  else:
    ans += m * float(380000)
print(ans)
