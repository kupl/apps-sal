n,k=[int(x) for x in input().rstrip().split()]
v=[int(x) for x in input().rstrip().split()]
vr=v[::-1]
ans=0
mi=min(n,k)

for i in range(mi+1):
  for j in range(mi-i+1):
    minus=0
    now=v[:i]+vr[:j]
    d=k-(len(now))
    now.sort()
    md=min(d,len(now))
    for s in range(md):
      if 0<=now[s]:
        break
      minus+=now[s]

    ans=max(ans,sum(now)-minus)
print(ans)
