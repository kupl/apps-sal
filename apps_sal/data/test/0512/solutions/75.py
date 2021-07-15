N=int(input())
X=[list(map(int,input().split())) for i in range(N)]
Y=[0]*(2*N+2)
for i in range(N):
  for j in range(2):
    Y[X[i][j]]+=1
if max(Y[1:2*N+1])>1:
  print('No')
  return
for i in range(N):
  if X[i][0]>X[i][1] and X[i][1]!=-1:
    print('No')
    return
X.sort(key=lambda x:max(x)%(N*3))
DP=[-1]*(N+1)
DP[N]=1
V=[N*3]*(N+1)
V[0]=0
C=0
Y=[-1]*(N*2+1)
for i in range(N):
  for j in range(2):
    if X[i][j]!=-1:
      Y[X[i][j]]=(i,j)
    else:
      X[i][j]=N*3
  if sum(X[i])==N*6:
    C+=1
def f(n,x):
  if x>C:
    return 0
  V[n]=min(x,V[n])
  if DP[n]!=-1:
    return DP[n]
  DP[n]=0
  for i in range(1,N-n+1):
    c=V[n]
    Z=[]
    for j in range(2*n+1,2*(n+i)+1):
      if Y[j]==-1:
        Z.append(-1)
        continue
      if min(X[Y[j][0]])<=2*n:
        Z=-1
        break
      Z.append(Y[j][0])
    if Z==-1:
      continue
    for j in range(i):
      if min(Z[j],Z[i+j])!=-1 and Z[j]!=Z[i+j]:
        Z=-1
        break
    if Z==-1:
      continue
    for j in range(i):
      if Z[j]!=-1 and X[Z[j]][1]!=N*3 and X[Z[j]][1]!=2*n+i+j+1:
        Z=-1
        break
      j+=i
      if Z[j]!=-1 and X[Z[j]][0]!=N*3 and X[Z[j]][0]!=2*n+j-i+1:
        Z=-1
        break
    if Z==-1:
      continue
    for j in range(i):
      if max(Z[j],Z[i+j])==-1:
        c+=1
    DP[n]|=f(n+i,c)
  return DP[n]

if f(0,0):
  print('Yes')
else:
  print('No')

