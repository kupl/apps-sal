INF=float('inf')
n,k,c=list(map(int,input().split()))
s=input()

L=[-1 for _ in range(n)]
cl=c+1
wl=1
for i in range(n):
  if wl>k:
    continue
  if s[i]=='x':
    cl+=1
  else:
    if cl>c:
      L[i]=wl
      wl+=1
      cl=1
    else:
      cl+=1

R=[-1 for _ in range(n)]
cr=c+1
wr=k
for j in range(n-1,-1,-1):
  if wr<1:
    continue
  if s[j]=='x':
    cr+=1
  else:
    if cr>c:
      R[j]=wr
      wr-=1
      cr=1
    else:
      cr+=1

for i in range(n):
  if L[i]==-1:
    continue
  if R[i]==-1:
    continue
  if L[i]==R[i]:
    print((i+1))
    

