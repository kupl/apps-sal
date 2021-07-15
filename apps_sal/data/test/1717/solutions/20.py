import math
n = int(input())
tem = 1

for i in range(1,n+1):
  tem = tem*i//(math.gcd(tem,i))
  
print(tem+1)
