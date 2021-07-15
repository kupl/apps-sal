import sys
readline=sys.stdin.readline
read=sys.stdin.read
 
h,w,d=map(int,readline().split())
a=[list(map(int,readline().split())) for _ in range(h)]
q,*lr=map(int,read().split())

ca=dict()
for i,l in enumerate(a):
  for j,e in enumerate(l):
    ca[e]=(i+1,j+1)
mp=[[0]*((h*w)//d+1) for _ in range(d)]
for i,mpl in enumerate(mp):
  for j,_ in enumerate(mpl[:-1]):
    if 0<i+d*j<=h*w-d:
      mpl[j+1]=mpl[j]+abs(ca[i+d*j][0]-ca[i+d*(j+1)][0])\
                +abs(ca[i+d*j][1]-ca[i+d*(j+1)][1])
for l,r in zip(*[iter(lr)]*2):
  print(mp[l%d][r//d]-mp[l%d][l//d])
