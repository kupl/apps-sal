n = int(input())
a = list(map(int,input().split()))
ls = [0]*20
for i in a:
  for j in range(20):
    if i&1<<j:
      ls[j] += 1
ans = 0
for i in range(n):
  x = 0
  for j in range(20):
    if ls[j]:
      x += 1<<j
      ls[j] -= 1
  ans += x**2
print(ans)
