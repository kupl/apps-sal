L=list()
R=list()
N,M=map(int,input().split())
for i in range(M):
  a,b=map(int,input().split())
  if a==1:
    L.append(b)
  elif b==1:
    L.append(a)
  if a==N:
    R.append(b)
  elif b==N:
    R.append(a)
L=set(L)
R=set(R)
if len(L&R)==0:
  print("IMPOSSIBLE")
else:
  print("POSSIBLE")
