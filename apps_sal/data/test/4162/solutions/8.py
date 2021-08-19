import math
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
r = 0
for ii in range(1, n):
    r = r * a[ii] // math.gcd(r, a[ii])


def func(x):
    y = 0
    for aa in a:
        y += x % aa
    return y


print(func(r - 1))
