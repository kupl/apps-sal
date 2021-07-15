import math
x,y=(list(map(int,input().strip().split(' '))))
if((x==y) or (x==2 and y==4) or(y==2 and x==4)):
  print("=")
else:
  t = y*math.log(x*1.0)
  tt = x*math.log(y*1.0)
  if(t>tt):
    print(">")
  else:
    print("<")


