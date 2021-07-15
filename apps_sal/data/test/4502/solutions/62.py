from collections import deque

n = int(input())
a = list(map(int, input().split()))
b = deque()
flip = False
for i, x in enumerate(a):
  if flip:
    b.appendleft(x)
  else:
    b.append(x)
  flip = not flip

if flip:
  b = list(reversed(b))
print(*b)  
