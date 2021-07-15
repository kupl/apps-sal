k = int(input())
from collections import deque
d = deque( )
d.append((1,1))
discovered = set()
while True:
  node, cost = d.popleft()
  discovered |= {node}
  if node == 0: 
  	print(cost)
  	return
  if (node*10)%k not in discovered:
    d.appendleft( ((node*10)%k  ,cost))
  if (node+1)%k not in discovered:
    d.append((node+1,cost+1))
