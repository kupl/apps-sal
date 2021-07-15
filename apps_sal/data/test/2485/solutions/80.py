h,w,m=map(int,input().split())
s=[0]*m
t=[0]*m
temp=set()
for i in range(m):
  sm,tm=map(int,input().split())
  s[i]=sm
  t[i]=tm
  temp.add((s[i],t[i]))
st=[0]*h
tt=[0]*w
for i in range(m):
  st[s[i]-1]=st[s[i]-1]+1
  tt[t[i]-1]=tt[t[i]-1]+1
smax=max(st)
tmax=max(tt)
ans=smax+tmax
maxs=[]
maxt=[]
for i in range(h):
  if st[i]==smax:
    maxs.append(i)
for i in range(w):
  if tt[i]==tmax:
    maxt.append(i)

if len(maxs)*len(maxt)>m:
  print(ans)
else:
  for i in range(len(maxs)):
    for j in range(len(maxt)):
      if (maxs[i]+1,maxt[j]+1) not in temp:
        print(ans)
        return
  else:
    print(ans-1)
