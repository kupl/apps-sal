s = input()
t = input()
x = len(s)
y = len(t)
ans = 10000
for i in range(x):
  if(i > x - y):
    break
  tm = 0
  for j in range(0, y):
    if(s[i + j] != t[j]):
      tm += 1
  ans = min(tm ,ans)
print(ans)

