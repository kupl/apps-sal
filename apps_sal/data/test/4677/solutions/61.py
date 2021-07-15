from collections import deque
d = deque()
for c in input():
  if c != 'B': d.append(c) 
  elif len(d) != 0: d.pop()
print(*d, sep='')
