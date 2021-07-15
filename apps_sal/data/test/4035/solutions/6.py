import math
import sys

a, b = map(int,input().split())

for i in range(10001):
        if math.floor(i * 0.08) == a and math.floor(i*0.1) == b:
            print(i)
            return
            
print('-1')
