n, a = map(int, input().split())
x = list(map(int, input().split()))

for i in range(n):
  x[i] -= a

d = [0] * 6000
ans = 0
for dif in x:
  ans += d[-dif+3000]
  if dif == 0:
    ans += 1
  if dif < 0:
    for i in range(6000):
      if 0 <= i+dif < 6000:
        d[i+dif] += d[i]
  else:
    for i in range(5999, -1, -1):
      if 0 <= i+dif < 6000:
        d[i+dif] += d[i]
  d[dif+3000] = d[dif+3000] + 1
  
print(ans)
