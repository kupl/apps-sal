W,H,x,y = map(int,input().split())

if x == W/2 and y == H/2:
  res = 1
else:
  res = 0
  
print(W*H/2,res)
