import math
sol = 0
p=int(input())
for e in range(1, p):
     if math.gcd(p-1, e) == 1:
          sol+=1
print(sol)
