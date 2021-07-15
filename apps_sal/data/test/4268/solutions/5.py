import math
n,d=list(map(int,input().split()))

x=[]
for i in range(n):
  x.append(list(map(int,input().split())))

cnt=0

for i in range(n-1):
  for j in range(i+1,n):
    s=0
    for k in range(d):
      s+=(x[i][k]-x[j][k])**2
    if int(math.sqrt(s))**2==s:
      cnt+=1
      
print(cnt)

