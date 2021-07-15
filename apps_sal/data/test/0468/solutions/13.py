from math import *
x,y=list(map(int,input().split()))
if y*log(x)-x*log(y)==00:
      print("=")
elif y*log(x)-x*log(y)>0:
      print(">")
else:
      print("<")
      

