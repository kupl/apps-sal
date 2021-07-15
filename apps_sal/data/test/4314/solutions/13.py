H,W=map(int,input().split())
L=[[] for i in range(H)]
yoko=list()
for i in range(H):
  L1=list(input())
  if L1==["."]*W:
    yoko.append(i)
  L[i]=L1
R=list(range(W))
for i in range(H):
  for j in range(W):
    if j in R and L[i][j]=="#":
      R.remove(j)
for i in range(H):
  if i in yoko:
    continue
  s=L[i]
  r=list()
  for j in range(W):
    if j not in R:
      r.append(s[j])
  print("".join(r))
