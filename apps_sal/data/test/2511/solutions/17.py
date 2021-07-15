import sys
sys.setrecursionlimit(100000)

N,K=list(map(int,input().split()))
MOD=10**9+7
branch=[[] for _ in range(N)]
for i in range(N-1):
  a,b=list(map(int,input().split()))
  branch[a-1].append(b-1)
  branch[b-1].append(a-1)

if K==1:
  if N==1:
    print((1))
  else:
    print((0))
  return
  
P=[0]*(K-1)
P[K-2]=K-2
for i in range(K-3,0,-1):
  P[i]=P[i+1]*i%MOD
  
def PPP(start,num):
  if start<num:
    return 0
  if start==K-2:
    return P[start-num+1]
  if start==K-1:
    return P[start-num+2]*(K-1)%MOD
  
ans=1

def draw(parent,nord):
  nonlocal ans
  children=len(branch[nord])-(parent !=-1)
  if children==0:
    return
  #(K-2)*(K-1)*... をchildrenの数だけ掛ける。
  ans=ans*PPP(K-1-(parent !=-1),children)%MOD
  for b in branch[nord]:
    if b != parent:
      draw(nord,b)

for i in range(len(branch[0])+1):
  ans=ans*(K-i)%MOD
for bra in branch[0]:
  draw(0,bra)
print(ans)

