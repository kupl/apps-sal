from collections import deque
N,M=map(int, input().split())
A=[[]for _ in range(N)]
V=[False]*N
X=[0]*N
x=0
for i in range(M):
  L,R,D=map(int, input().split())
  A[L-1].append((R-1,D))
  A[R-1].append((L-1,-D))
  
for i in range(N):
  if V[i]==False:
    stack=deque([(i,x)])
    V[i]=True
    while stack:
      now,dx=stack.popleft()
      for new,di in A[now]:
        if V[new]:
          if X[new]!=dx+di:
            print('No')
            return
        else:
          X[new]=dx+di
          V[new]=True
          stack.append((new,dx+di))

if max(X)-min(X)>10**9:
  print('No')
else:
  print('Yes')
