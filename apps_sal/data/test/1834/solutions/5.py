'''
' Title:	
' Author:	Cheng-Shih, Wong
' Date:		
'''

import math

n = int(input())
a = [int(v) for v in input().split()]

a.sort()
half = math.ceil(n / 2)
b = [0] * n

for i in range(0, half):
    b[i * 2] = a[i]
for i in range(half, n):
    b[(i - half) * 2 + 1] = a[i]

print(' '.join([str(v) for v in b]))
