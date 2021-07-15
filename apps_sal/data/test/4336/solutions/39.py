W, H, x, y = map(int, input().split())
 
if x == W / 2 and y == H / 2:
  print((W * H) / 2, 1)
else:
  print((W * H) / 2, 0)
