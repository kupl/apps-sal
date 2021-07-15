import cmath
import math

N = int(input())
pc = []
for i in range(N):
  x, y = map(int, input().split())
  c = x + y*1j
  p = cmath.phase(c)
  pc.append([p, c])
pc = sorted(pc, key=lambda x: x[0])

ps = [pc[i][0] for i in range(N)]
cs = [pc[i][1] for i in range(N)]

def L(i, j, N):
  if i<j:
    return list(range(i, j))
  else:
    return list(range(0, j)) + list(range(i+1, N))

s = 0
m = 0

for start in range(N):
  for end in range(N):
    s = 0
    #print(start,end,N,L(start,end,N))
    for k in L(start,end,N):
      s += cs[k]
    m = max(m, abs(s))
s = 0
for k in range(N):
  s += cs[k]
  m = max(m, abs(s))
print(m)
