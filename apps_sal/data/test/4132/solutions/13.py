import sys
import math


inint = lambda: int(sys.stdin.readline())
inintm = lambda: list(map(int, sys.stdin.readline().split()))
inintl = lambda: list(inintm())
instrm = lambda: list(map(str, sys.stdin.readline().split()))
instrl = lambda: list(instrm())

n = inint()
A = inintl()

m = min(A)

mod_min = 10**9

for a in A:
    if a % m == 0:
        continue
    mod_min = min(mod_min, a % m)

if mod_min == 10**9:
    print(m)
else:
    print((math.gcd(m, mod_min)))

