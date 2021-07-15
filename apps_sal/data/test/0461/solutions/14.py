n=int(input())
a=int(input())
b=int(input())
c=int(input())
if(n==1):
  print(0)
else:
  dist=[a,b,c]
  dist.sort()
  min1=dist[0]
  min2=dist[1]
  min3=dist[2]
  if(min1==a or min1==b):
    print((n-1)*min1)
  else:
    print(min2+((n-2)*min1))
