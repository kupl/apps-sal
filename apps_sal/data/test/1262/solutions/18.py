import sys
input=sys.stdin.readline
n=int(input())
X=[[0]*7 for _ in range(n)]
for i in range(n):
  x,y=map(int,input().split())
  X[i][0],X[i][1],X[i][2]=i+1,x,y
C=[int(i) for i in input().split()]
K=[int(i) for i in input().split()]
for i in range(n):
  X[i][3],X[i][4]=C[i],K[i]

ans_am=0
ans_ps=0
Ans=[]
ans_con=0
Con=[]

def m(X):
  ret=0
  cur=X[0][3]
  for i in range(1,len(X)):
    if X[i][3]<cur:
      ret=i
      cur=X[i][3]
  return ret

def cost(k,ki,x,xi,y,yi):
  return (k+ki)*(abs(x-xi)+abs(y-yi))

while X:
  r=m(X)
  ind,x,y,c,k,flag,source=X.pop(r)
  ans_am+=c
  if not flag:
    ans_ps+=1
    Ans.append(ind)
  else:
    ans_con+=1
    Con.append((ind,source))
  for i in range(len(X)):
    indi,xi,yi,ci,ki,flagi,sourcei=X[i]
    co=cost(k,ki,x,xi,y,yi)
    if co<ci:
      X[i][3],X[i][5],X[i][6]=co,1,ind

print(ans_am)
print(ans_ps)
print(*Ans)
print(ans_con)
for i,j in Con:
  print(i,j)
