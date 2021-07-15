N,C=map(int,input().split())
xc=[tuple(map(int,input().split())) for i in range(N)]
xc.sort()
ans=0
p=0
#右を取る範囲と左を取る範囲を決めればいい
s=[0]*(N+1)#時計回り
ss=[0]*(N+1)#反時計回り
for i in range(N):
  s[i+1]=s[i]+xc[i][1]

for i in range(N):
  ss[i+1]=ss[i]+xc[N-1-i][1]
maxs=[0]*(N+1)
maxss=[0]*(N+1)
for i in range(N):
  s[i+1]=s[i+1]-xc[i][0]
  ss[i+1]=ss[i+1]-(C-xc[N-1-i][0])
  maxs[i+1]=max(maxs[i],s[i+1])
  maxss[i+1]=max(maxss[i],ss[i+1])
ans=max(0,maxs[-1])
ans=max(ans,maxss[-1])
for i in range(N):
  if s[i+1]>xc[i][0]:
    ans=max(ans,maxss[N-i-1]+(s[i+1]-xc[i][0]))
  if ss[i+1]>(C-xc[N-1-i][0]):
    ans=max(ans,maxs[N-i-1]+(ss[i+1]-(C-xc[N-1-i][0])))
print(ans)
