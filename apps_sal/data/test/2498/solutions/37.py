import queue
import numpy as np
import math

N, M = map(int, input().split())
a2 = list(map(int, input().split()))
a = []
for i in a2:
    a.append(i//2)

lcm = a[0]

for i in a:
    lcm *= i // math.gcd(lcm, i)

hasAns = True
for i in a:
    if (lcm // i) % 2 == 0:
        hasAns = False
        break

ans = 0

if hasAns:
    ans = ((M // lcm) + 1 )// 2

print(ans)
