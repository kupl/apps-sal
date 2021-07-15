import sys
readline = sys.stdin.readline
 
N,M = map(int,readline().split())
from collections import defaultdict
tasks = defaultdict(list)
for i in range(N):
  a,b = map(int,readline().split())
  tasks[a].append(b)
  
import heapq as hq
q = []
ans = 0
for i in range(1, M + 1):
  newtask = tasks[i]
  for t in newtask:
    hq.heappush(q,-t)
  if q:
    ans += -hq.heappop(q)
 
print(ans)
