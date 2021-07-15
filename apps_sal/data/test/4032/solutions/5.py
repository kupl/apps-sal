from collections import deque
n,k=map(int,input().split())
x=deque()
for j in map(int,input().split()):
  x.append(j)
while x:
  if x[0]<=k: x.popleft()
  else: break
while x:
  if x[-1]<=k: x.pop()
  else: break
print(n-len(x))
