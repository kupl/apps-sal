from collections import deque
s = deque(input())
q = int(input())
rev = False

for i in range(q):
  query = input().split()
  
  if query[0] == '1':
    rev = not rev
  else:
    if query[1] == '1':
      if rev: 
        s.append(query[2])
      else:
        s.appendleft(query[2])
    elif query[1] == '2':
      if rev:
        s.appendleft(query[2])
      else:
        s.append(query[2])
s = list(s)
if rev:
  s = s[::-1]

print(*s, sep='')
