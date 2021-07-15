import math

a, b = input().split()
c = int(a + b)

for i in range(int(math.sqrt(c))+1):
  if c == i*i:
    print("Yes")
    break
else:
  print("No")
  

