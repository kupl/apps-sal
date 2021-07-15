a,b,c=map(int,input().split())
if a>=b and a>=c:
  print(10*a+b+c)
elif  b>=a and b>=c:
  print(a+10*b+c)
else:
  print(a+b+10*c)
