from collections import defaultdict

d = defaultdict(int)
d=[0]*3
n = int(input())

for i in list(map(int, input().split())):
  if i % 4 == 0:
    d[2] += 1
  elif i % 2 == 0:
    d[1] += 1
  else:
    d[0] += 1
t = d[2] - d[1]
if (d[0] <= d[2]) or ((d[0] == d[2] + 1) and (d[1] == 0)):
  print("Yes")
else:
  print("No")

