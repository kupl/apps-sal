from itertools import product


n,m = map(int, input().split())

switch = []

for i in range(m):
  k, *s = map(int, input().split())
  s = list(s)
  switch.append(s)

p = list(map(int, input().split()))
ans = 0

for i in product(range(2), repeat=n):
  flag = True
  for s in range(m):
    cnt = 0
    for t in switch[s]:
      if i[t-1] == 1:
        cnt += 1
    if cnt % 2 != p[s]:
      flag = False
      break
  if flag == True:
    ans += 1

print(ans)
