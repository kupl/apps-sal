import math

a, b = input().split()
n = int(a + b)

if n == round(math.sqrt(n))**2:
    print('Yes')
else:
    print('No')
