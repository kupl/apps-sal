n,m=list(map(int,input().split()))
pref=[[] for _ in range(n+1)]
py = [[i]+list(map(int,input().split())) for i in range(m)]
py.sort(key=lambda x: (x[1],x[2]))
ans=list()
now=0
cnt=0
for x in py:
  cnt = 1 if now != x[1] else cnt + 1
  now = x[1]
  ans.append([x[0],x[1],cnt])
ans.sort(key=lambda x:x[0])
for x in ans:
  print((str(x[1]).zfill(6)+str(x[2]).zfill(6)))



