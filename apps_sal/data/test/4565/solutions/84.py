from collections import deque

N=int(input())
S=input()

left=deque([0])
right=[0]
for i in range(N):
  if S[i]=='W':plus=1
  else:plus=0
  left.append(left[-1]+plus)
  if S[-i-1]=='E':plus=1
  else:plus=0
  right.append(right[-1]+plus)
  
left.popleft()
right = right[::-1]
right.pop()

print(min([left[i]+right[i] for i in range(N)])-1)
