x,y,z=map(int,input().split())
n=0
while True:
  if n*y+(n+1)*z>x:
    print(n-1)
    return
  n+=1
