import math
s,p = map(int,input().split())
b,c = -s,p

tmp1 = (-b + math.sqrt(b ** 2 - 4 * c)) / 2
tmp2 = (-b - math.sqrt(b ** 2 - 4 * c)) / 2

n1 = s - tmp1
n2 = s - tmp2

check = False
if int(n1) == n1 and n1 > 0:
  check = True
if int(n1) == n2 and n2 > 0:
  check = True
  
print("Yes" if check else "No")
