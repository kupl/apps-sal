h,w,d=map(int,input().split())
l=[[] for t in range(h*w)]
for i in range(h):
  ll=list(map(int,input().split()))
  for j in range(w):
    l[ll[j]-1]=[i,j]
    
r=[[0] for dd in range(d)]
for dd in range(d):
  if dd==0:
    k=d
  else:
    k=dd
  while k+d<=h*w:
    r[dd].append(r[dd][-1]+abs(l[k+d-1][0]-l[k-1][0])+abs(l[k+d-1][1]-l[k-1][1]))
    k+=d

    
q=int(input())
for qq in range(q):
  a,b=map(int,input().split())
  if a%d==0:
    p=d
  else:
    p=a%d
  aa=(a-p)//d
  bb=(b-p)//d
  ans=r[a%d][bb]-r[a%d][aa]
  print(ans)
