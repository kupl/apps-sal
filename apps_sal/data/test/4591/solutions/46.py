A,B,C,X,Y = list(map(int,input().split()))
if A+B<=2*C:
  print((A*X+B*Y))
else:
  if X>=Y:
    if 2*C*Y+A*(X-Y)>=2*C*X:
      print((2*C*X))
    else:
      print((2*C*Y+A*(X-Y)))
  else:
    if 2*C*X+B*(Y-X)>=2*C*Y:
      print((2*C*Y))
    else:
      print((2*C*X+B*(Y-X)))

