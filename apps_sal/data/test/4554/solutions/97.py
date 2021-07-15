W,a,b=map(int,input().split())
if b>a:
  if b-(a+W)<=0:
  	print(0)
  	return
  print(b-(a+W))
else:
  if a-(b+W)<=0:
  	print(0)
  	return
  print(a-(b+W))
