from collections import deque
d = deque()
for w in input():
  d.remove(w) if w in d else d.append(w) 
print(['Yes','No'][len(d)!=0])
