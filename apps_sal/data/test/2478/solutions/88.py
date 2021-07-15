from collections import deque

n=int(input())
s=deque(input())


left=0
right=0
for i in range(n):
  if s[i]=="(":
    left+=1
  else:
    if left>0:
      left-=1
    else:
      right+=1
    
      

for _ in range(left):
    s.append(")")
    

for _ in range(right):
    s.appendleft("(")

print("".join(s))
