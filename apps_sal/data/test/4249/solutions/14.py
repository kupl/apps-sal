n, m = list(map(int, input().split()))

l = list(map(int,input().split()))

l.sort(reverse = True)

left = 1
right = n

def check(k,m):
  if m > 0:
    lef = 0
    z = 0
    for i in range(n):
      m -= max(0, l[i]-lef)
      z += 1
      if z == k:
        z = 0
        lef += 1
  if m <= 0:
    return 1
  else:
    return 0

res = []

while left <= right:
  mid = int((left+right)/2)
  if check(mid, m):
    res.append(mid)
    right = mid - 1
  else:
    left = mid + 1
if len(res) > 0:
  print(min(res))
else:
  print("-1")

"""
n, m = map(int, input().split())

l = list(map(int,input().split()))

s = sum(l)
ans = 0

def find(x):
  su = 0
  days = 0
  z = 0

  for i in l:
    su += max(0, i-z)
    days += 1
    if days == x:
      days = 0
      z += 1
  if su < m:
    return 0
  return x

def binary(left, right):
  nonlocal ans
  mid = int((left+right)/2)
  r = find(mid)
  if right == left:
    ans = r
  elif left == right - 1:
    if r:
      ans = r
    else:
      binary(r, r)
  else:
    if r:
      binary(left, mid)
    else:
      binary(mid, right)

if s < m:
  print("-1")
elif s == m:
  print(n)
else:
  l.sort(reverse = True)
  binary(1,n)
  print(ans)
print(ans)
"""

