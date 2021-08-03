import sys
import math
n, k = list(map(int, sys.stdin.readline().split()))
a, b = list(map(int, sys.stdin.readline().split()))
factors = []
dis = n * k
start = a
nax, nin = -1, 1e12 + 1
for i in range(n):
    b1 = k * i + b
    if b1 > a:
        l = b1 - a
    else:
        l = dis - (a - b1)
    if l != 0:
        lcm = (dis * l) // (math.gcd(dis, l))
        nax = max(nax, lcm // l)
        nin = min(nin, lcm // l)
st = k - a
for i in range(n):
    b1 = k * i + b
    if b1 > st:
        l = b1 - st
    else:
        l = dis - (st - b1)
    if l != 0:
        lcm = (dis * l) // (math.gcd(dis, l))
        nax = max(nax, lcm // l)
        nin = min(nin, lcm // l)
print(nin, nax)
