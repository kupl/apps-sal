import sys
from collections import deque
# sys.stdin = open("ivo.in")
n, b = map(int, sys.stdin.readline().split())
b += 1
q = deque()
res = []
cur_time = 0
for iter in range(n):
  t, d = map(int, sys.stdin.readline().split())
  while len(q) > 0 and q[0] <= t:
    q.popleft()
  if len(q) >= b:
    res.append(-1)
    continue
  if len(q) == 0:
    res.append(t + d)
    q.append(t + d)
  else:
    res.append(q[-1] + d)
    q.append(q[-1] + d)
print(" ".join(map(str, res)))
