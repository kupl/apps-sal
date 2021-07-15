from math import *
def lInt(d = None): return list(map(int, input().split(d)))
n, *_ = lInt()
a = list(lInt())
is_sq = [0]*n
sq = 0; ans = 0
pos = []

def closest(v):
  w = sqrt(v)
  f = floor(w)
  c = f+1
  fsq = f*f
  csq = c*c

  fd = v-fsq
  cd = csq-v
  return min(fd, cd)
  
def isS(v):
  w = int(sqrt(v))
  return w*w == v

for i, v in enumerate(a):
  w = int(sqrt(v))
  
  if w*w == v:
    is_sq[i] = 1
    sq += 1

if sq > n//2:
  for i, v in enumerate(a):
    if is_sq[i] and sq > n//2:
      if a[i]:
        ans += 1
        sq -= 1
        is_sq[i] = 0
  for i, v in enumerate(a):
    if is_sq[i] and sq > n//2:
      ans += 2
      sq -= 1
elif sq < n//2:
  for i, v in enumerate(a):
    if not is_sq[i]:
      pos.append(closest(a[i]))
  pos.sort()
  for j in range(n//2-sq):
    ans += pos[j]
else:
  ans = 0
print(ans)

