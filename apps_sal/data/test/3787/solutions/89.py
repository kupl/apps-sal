N,A,B=map(int,input().split())
if A+B-1>N or A*B<N:
  print(-1)
  return
Q=[[] for i in range(B)]
for i in range(N):
  Q[i//A].append(i+1)
Q=Q[::-1]
X=N-1
for i in range(B):
  if len(Q[i])==0:
    Q[i].append(Q[-(X//A+1)][-1])
    del Q[-(X//A+1)][-1]
    X-=1
  else:
    break
P=[]
for i in range(B):
  for j in range(len(Q[i])):
    P.append(Q[i][j])
print(*P)
