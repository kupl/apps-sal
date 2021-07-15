import math
a,b = list(map(str,input().split()))
c = int(a+b)
if int(math.sqrt(c))**2 == c:
  print("Yes")
else:
  print("No")

