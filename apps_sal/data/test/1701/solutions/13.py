n,m=map(int,input().split())
d={}
for _ in range(n):
  name,ip=input().split()
  d[ip]=name
for _ in range(m):
  s=input()
  ip=s.split()[-1]
  if ip[-1]==';':
    ip=ip[:-1]
  print(s,"#"+d[ip])
