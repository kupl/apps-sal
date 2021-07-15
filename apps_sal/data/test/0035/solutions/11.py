from copy import deepcopy
n, m = map(int, input().split())

l = [0 for i in range(n)]

for i in range(n):
  l[i] = input()
# print(l)

f1 = 0
f2 = 0
for i in range(n):
  cnt = [0, 0, 0]
  for j in range(m):
    if (l[i][j] == 'R'):
      cnt[0] += 1
    if (l[i][j] == 'G'):
      cnt[1] += 1
    if (l[i][j] == 'B'):
      cnt[2] += 1
  if not ((cnt[0] == 0 and cnt[1] == 0) or (cnt[1] == 0 and cnt[2] == 0) or (cnt[2] == 0) and cnt[0] == 0):
    f1 = 1

for j in range(m):
  cnt = [0, 0, 0]
  for i in range(n):
    if (l[i][j] == 'R'):
      cnt[0] += 1
    if (l[i][j] == 'G'):
      cnt[1] += 1
    if (l[i][j] == 'B'):
      cnt[2] += 1
  if not ((cnt[0] == 0 and cnt[1] == 0) or (cnt[1] == 0 and cnt[2] == 0) or (cnt[2] == 0) and cnt[0] == 0):
    f2 = 1

if (f1 == 1 and f2 == 1):
  print('NO')
  return
if (f2 == 0):
  l1 = [[0 for i in range(n)] for j in range(m)]
  for i in range(n):
    for j in range(m):
      l1[j][i] = l[i][j]
  n, m = m, n
  l = deepcopy(l1)

r = []
g = []
b = []
for i in range(n):
  if (l[i][0] == 'R'):
    r.append(i)
  if (l[i][0] == 'G'):
    g.append(i)
  if (l[i][0] == 'B'):
    b.append(i)
ans = 0
if (len(r) != len(g) or len(r) != len(b) or len(r) != len(g)):
  ans = 1
for i in range(len(r) - 1):
  if (r[i+1] - r[i] != 1):
    ans = 1
for i in range(len(g) - 1):
  if (g[i+1] - g[i] != 1):
    ans = 1
for i in range(len(b) - 1):
  if (b[i+1] - b[i] != 1):
    ans = 1
if (ans == 1):
  print('NO')
  return
print('YES')
