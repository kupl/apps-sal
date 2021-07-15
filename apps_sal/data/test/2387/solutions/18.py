import sys
input = sys.stdin.readline
n = int(input())
chk = []
res = []
for i in range(n):
  s = input().strip()
  m = 0
  e = 0
  for i in s:
    if i == ')':
      e -= 1
      m = min(m,e)
    else:
      e += 1
  if e >= 0:
    chk.append((m,e))
  else:
    res.append((-1*e+m,-1*e))
  
from operator import itemgetter
res.sort(key=itemgetter(0),reverse=True)
chk.sort(key=itemgetter(0),reverse=True)
ans = 'Yes'
st = 0
for i,j in chk:
  if i+st < 0:
    ans = 'No'
    break
  st += j
  
sr = 0
for i,j in res:
  if i+sr < 0:
    ans = 'No'
    break
  sr += j
  
if st != sr:
  ans = 'No'

print(ans)
