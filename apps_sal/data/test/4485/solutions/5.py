n, m = [int(x) for x in input().split()]
a = []
for i in range(m):
  a.append([int(x) for x in input().split()])
  
res = "IMPOSSIBLE"
flag = []

for i in range(m):
  if a[i][0] == 1:
    flag.append(a[i][1])
flag = set(flag)

for i in range(m):
  if a[i][0] in flag and a[i][1] == n:
    res = "POSSIBLE"
print(res)
