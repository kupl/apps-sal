x = int(input())
ans = 0
k = 0
t = 0
while k < x:
  k = t * (t + 1) / 2
  t += 1
ans = t - 1
print(ans)
