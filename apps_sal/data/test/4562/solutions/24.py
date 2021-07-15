from math import sqrt
n=int(input())
for i in range(1,int(sqrt(n))+1):
  if i**2>n:
    print((i-1)**2)
    break
else:
  print(i**2)
