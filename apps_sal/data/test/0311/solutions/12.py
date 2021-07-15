x, y, z, t1, t2, t3=map(int,input().split())
if abs(y-x)*t1<(abs(x-z)*t2+abs(y-x)*t2+3*t3):
  print ("NO")
else:
  print ("YES")
