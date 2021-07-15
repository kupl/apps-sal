import collections
import math

N, A, B = list(map(int, input().split()))
v = list(map(int, input().split()))
d = list(reversed(sorted(v)))
c = collections.Counter(v)

start = A
end = A
if c[d[0]] >= A:
  end = min(c[d[0]], B)
  
ans = 0
ans_com = 0
for i in range(start, end+1):
  sel = i
  com = 1
  total = 0
  for j in range(len(d)):
    p = c[d[j]]
    com *= math.factorial(p)
    total += d[j] * p
    if sel <= p:
      com /= (math.factorial(sel) * math.factorial(p-sel))
      total -= d[j] * (p - sel)
      break
    sel -= p
  ave = total / i
  ans = ave
  ans_com += int(com)
print(ans)
print(ans_com)

