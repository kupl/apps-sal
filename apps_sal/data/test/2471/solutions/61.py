H,W,N=map(int,input().split())
D=dict()
for i in range(N):
  a,b=map(int,input().split())
  for p in range(-1,2):
    for q in range(-1,2):
      x=a+p
      y=b+q
      if 2<=x<=H-1 and 2<=y<=W-1:
        pos=(x,y)
        if pos in D:
          D[pos]+=1
        else:
          D[pos]=1
ans=[0]*10
V=list(D.values())
for v in V:
  ans[v]+=1
ans[0]=(H-2)*(W-2)-sum(ans)
print(*ans,sep='\n')
