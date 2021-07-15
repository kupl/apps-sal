N=int(input())
zls=[0 for _ in range(N)]
wls=[0 for _ in range(N)]
for i in range(N):
  x,y=[int(s) for s in input().split()]
  zls[i]=x+y
  wls[i]=x-y
print(max([max(zls)-min(zls),max(wls)-min(wls)]))
