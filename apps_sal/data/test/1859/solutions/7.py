import math
import sys
n = int(input())

for i in range(2,int(math.sqrt(n)) + 1):
    if n%i == 0:
        print(int((n - i)/2 + 1))
        return
print(1)

