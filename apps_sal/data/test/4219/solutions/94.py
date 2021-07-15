from itertools import product

n = int(input())

d = {}
for i in range(n):
  a = int(input())
  for _ in range(a):
    x, y = map(int, input().split())
    if i + 1 not in d:
      d[i + 1] = []
    d[i + 1].append((x, y))

ret = 0
for x in product((0, 1), repeat=n):
  ok = True
  for i in range(n):
    if x[i] == 0 or i + 1 not in d:
      continue
    for p, tf in d[i + 1]:
      if x[p - 1] != tf:
        ok = False
        break
    if not ok:
      break
  if ok:
    ret = max(ret, sum(x))

print(ret)
