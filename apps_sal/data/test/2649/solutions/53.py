n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
a=10**9
z_max=-1*a
z_min=a
w_max=-1*a
w_min=a
for x,y in l: #点のx座標とy座標の和の最大値と最小値の差か座標の差の最大値と最小値の差が答え
  z_max=max(z_max,x+y)
  z_min=min(z_min,x+y)
  w_max=max(w_max,x-y)
  w_min=min(w_min,x-y)
print(max(z_max-z_min,w_max-w_min))
