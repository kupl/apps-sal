from collections import Counter
n,m = map(int,input().split())
grid = [list(input()) for i in range(n)]
def jc(a,b):
  l = len(a)
  used = [0]*l
  for i in range(l):
    if used[i]:
      continue
    for j in range(i+1,l):
      if used[j]:
        continue
      if a[i] == b[j] and b[i] == a[j]:
        used[i] = 1
        used[j] = 1
        break
  if used.count(0) <= l%2:
    return True
  else:
    return False
def judge(a):
  h = len(a)
  w = len(a[0])
  used = [0]*h
  for i in range(h):
    if used[i]:
      continue
    ci = Counter(a[i])
    for j in range(i+1,h):
      if used[j]:
        continue
      cj = Counter(a[j])
      if ci == cj:
        if jc(a[i],a[j]):
          used[i] = 1
          used[j] = 1
          break
  if used.count(0) <= h%2:
    return True
  else:
    return False
gt = list(zip(*grid))
if judge(grid) & judge(gt):
  print("YES")
else:
  print("NO")
