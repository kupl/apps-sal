import math
from fractions import gcd
x = 0
n = int(input())
for i in range(2, int(math.sqrt(n+1))+2):
    for j in range(1+i%2, i, 2):
        if math.sqrt(i*i+j*j)>n:
            break
        if gcd(i, j) == 1:
            x+=int(n/(i*i+j*j))
print(x)
