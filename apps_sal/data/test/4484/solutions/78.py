from math import factorial
n,m=map(int,input().split())
l=10**9+7
if abs(n-m)>1:
  print(0)
  return
if abs(n-m)==1:
  print((factorial(n)*factorial(m))%l)
else:
  print(((factorial(n)**2)*2)%l)
