import math

n = int(input())
lim = int(math.sqrt(n))

for a in range(lim, 0, -1):
    b = n / a
    if b == int(b):
        print(a, int(b))
        break
