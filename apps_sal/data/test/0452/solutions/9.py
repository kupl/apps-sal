import math
import sys


def gcd(x, y):
    if(y == 0):
        return x
    else:
        return gcd(y, x % y)


p, q = list(map(int, sys.stdin.readline().split()))
n = int(input())
a = [0] * n
b = list(map(int, sys.stdin.readline().split()))
l = 0
for i in b:
    a[l] = i
    l = l + 1
x, y = a[n - 1], 1
for i in range(n - 2, -1, -1):
    x, y = y, x
    x = x + y * a[i]
g1 = gcd(p, q)
g2 = gcd(x, y)
p = p // g1
q = q // g1
x = x // g2
y = y // g2
if(x == p and y == q):
    print("YES")
else:
    print("NO")
