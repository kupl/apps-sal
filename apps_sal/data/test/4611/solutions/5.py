N = int(input())
T = []
XY = []
ans = "Yes"

for i in range(N):
  t,x,y = map(int,input().split())
  T.append(t)
  XY.append([x,y])

if T[0]>=abs(XY[0][0])+abs(XY[0][1]) and T[0]%2==(abs(XY[0][0])+abs(XY[0][1]))%2:
  None
else:
  ans = "No"

for i in range(1,N):
  dT=T[i]-T[i-1]
  dX=abs(XY[i][0]-XY[i-1][0])
  dY=abs(XY[i][1]-XY[i-1][1])
  if dT >= dX+dY and dT%2 == (dX+dY)%2:
    None
  else:
    ans = "No"

print(ans)
