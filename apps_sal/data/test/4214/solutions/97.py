import math
n=int(input())
XY=[list(map(int,input().split())) for _ in range(n)]
ans=0
for i in range(n-1):
  for j in range(i+1,n):
    disx=XY[i][0]-XY[j][0]
    disy=XY[i][1]-XY[j][1]
    dis=math.sqrt(disx**2+disy**2)

    ans+=dis

print(2*ans/n)
