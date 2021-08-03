import math

x = [int(i) for i in input().split()]
n = x[0]
m = x[1]
if(n % 2 == 0):
    s = math.ceil((n // 2) / m)
else:
    s = math.ceil(((n + 1) // 2) / m)

if(s * m <= n):
    print(s * m)
else:
    print(-1)
