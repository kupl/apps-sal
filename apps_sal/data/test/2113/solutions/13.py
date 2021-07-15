n=int(input());f=lambda u,v:u.append(v);l=[0]*n;d=[[]for _ in range(n)];l[0]=1;c=[1]
for _ in range(n-1):
  a,b=list(map(int,input().split()));f(d[a-1],b);f(d[b-1],a)
while c:
  x=c.pop()
  for y in d[x-1]:
    if not l[y-1]:
      f(c,y);l[y-1]=-1*l[x-1]
r=l.count(1);print(r*(n-r)-n+1)

