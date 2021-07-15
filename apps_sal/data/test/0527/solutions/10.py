s=input()
t=input()
ds={}
for i in range(len(s)):
  if s[i] in ds:
    ds[s[i]].append(i+1)
  else:
    ds[s[i]]=[i+1]
n=len(s)
now=0 # mod n
ans=0
from bisect import bisect_right
for ti in t:
  if ti not in ds:
    print((-1))
    return
  tmp=bisect_right(ds[ti],now)
  if tmp==len(ds[ti]):
    get=n+ds[ti][0]
  else:
    get=ds[ti][tmp]
  ans+=get-now
  #print(now,get)
  now=(get)%n
print(ans)
#print(ds)

