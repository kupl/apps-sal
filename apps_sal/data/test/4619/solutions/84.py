w,h,n = [int(x) for x in input().split()]
a = []
for i in range(n):
  a.append([int(x) for x in input().split()])

mp = [[0] * h for x in range(w)]

for i in range(n):
  if a[i][2] == 1:
    for j in range(a[i][0]):
      for k in range(h):
        mp[j][k] = 1
  elif a[i][2] == 2:
    for j in range(a[i][0],w):
      for k in range(h):
        mp[j][k] = 1
  elif a[i][2] == 3:
    for j in range(w):
      for k in range(a[i][1]):
        mp[j][k] = 1
  elif a[i][2] == 4:
    for j in range(w):
      for k in range(a[i][1],h):
        mp[j][k] = 1

res = 0
for i in range(w):
  for j in range(h):
    if mp[i][j] == 0:
      res += 1

print(res)
