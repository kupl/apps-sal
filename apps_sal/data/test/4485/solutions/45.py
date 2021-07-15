n,m=map(int,input().split())
A=[]
B=[]
for i in range(m):
  a,b=map(int,input().split())
  if a==1:
    A.append(b)
  if b==n:
    B.append(a)
if len(set(A) & set(B))>0:
  print("POSSIBLE")
else:
  print("IMPOSSIBLE")
