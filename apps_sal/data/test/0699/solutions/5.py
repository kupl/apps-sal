import sys
import math

y, k, n = [int(x) for x in (sys.stdin.readline()).split()]

t = []

p = int(n / k)
z = p * k - y
if(z <= 0):
    print(-1)
    return

t.append(str(z))
while(z - k > 0):
    z -= k
    t.append(str(z))

print(" ".join(t[::-1]))
