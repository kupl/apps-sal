from sys import stdin
from math import hypot
r, d = [int(i) for i in stdin.readline().split()]
r1 = r - d
n = int(stdin.readline())
ans = 0
eps = 0.0000001

def ge0(a):
    return (a >= 0 or abs(a) <= eps)

for i in range(n):
    x, y, r2 = [int(i) for i in stdin.readline().split()]
    d = hypot(x, y)
    if ge0(d - r1 - r2) and ge0(r - d - r2):
        ans += 1

print(ans)
    

