n,m=map(int,input().split())
lange=[1]*(n+1)
for i in range(1,n+1):
  a=i
  b=n-a
  if lange[a]:lange[b]=0
langes=[]
for i in range(1,n):
  if lange[i]:
    if len(langes)%2:langes.append(i)
    else:langes.append(n-i)
langes.sort(reverse=1)
for i in range(m):print(i+1,i+1+langes[i])
