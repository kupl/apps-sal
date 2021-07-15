import math
n = int(input())

x,y = n,1 
for i in range(int(math.sqrt(n)),0,-1):
  if n%i == 0 :
    if x+y > i+n//i:
      x = i
      y = n//x
      
print(x-1+y-1)
