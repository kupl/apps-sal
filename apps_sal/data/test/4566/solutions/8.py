n,m=list(map(int,input().split()))
al=[]
bl=[]
for i in range(m):
  a,b=list(map(int,input().split()))
  al.append(a)
  bl.append(b)

for i in range(1,n+1):
  print((al.count(i)+bl.count(i)))

