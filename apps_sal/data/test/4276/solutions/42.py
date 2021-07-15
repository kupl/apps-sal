n,t=map(int,input().split())
a=[list(map(int,input().split())) for i in range(n)]
c=[]
for i in range(n):
  if a[i][1]<=t:
    c.append(a[i][0])

if not c:
  print('TLE')
else:
  print(min(c))
