import sys
import math

n = int(input())

for i in range(n):
    r, b, k = map(int, input().split())

    if r > b:
        r, b = b, r
    
    lcm = r * b // math.gcd(r,b)
    if (b - math.gcd(r, b) - 1) // r + 1 >= k:
        print("REBEL")
    else:
        print("OBEY")
