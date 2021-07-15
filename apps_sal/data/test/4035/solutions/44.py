import math,sys

A,B = map(int,input().split())

for price in range(1,100000):
    if math.floor(price*0.08) == A and math.floor(price*0.1) == B:
        print(price)
        return

print(-1)
