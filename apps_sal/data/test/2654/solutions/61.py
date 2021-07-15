N=int(input())
l,r=[],[]
for i in range(N):
  a,b=map(int,input().split())
  l.append(a)
  r.append(b)
l.sort()
r.sort()
if N%2:
  print(r[N//2]-l[N//2]+1)
else:
  a=(l[N//2]+l[N//2-1])/2
  b=(r[N//2]+r[N//2-1])/2
  print(int((b-a)*2)+1)
