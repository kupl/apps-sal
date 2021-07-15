H,W,N=map(int,input().split())
sita,hidari=0,0
ue,migi=W,H
for i in range(N):
  x,y,a=map(int,input().split())
  if a==1:
    hidari=max(x,hidari)
  elif a==2:
    migi=min(migi,x)
  elif a==3:
    sita=max(sita,y)
  else:
    ue=min(ue,y)
print(max(0,(migi-hidari))*max(0,(ue-sita)))
