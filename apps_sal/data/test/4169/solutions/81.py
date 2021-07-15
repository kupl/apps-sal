n,m=map(int,input().split())
a=[]
for _ in range(n):
  b=list(map(int,input().split()))
  a.append(b)
  
a.sort(key=lambda x: x[0])
ans=0
h=0

for y in a:
  d=y[0]
  e=y[1]
  if h+e>m:
    ans+=(m-h)*d
    h+=(m-h)
  else:
    h+=e
    ans+=d*e

print(ans)
