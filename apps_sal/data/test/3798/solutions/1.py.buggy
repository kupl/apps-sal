import math
import sys
n = int(input())
s = int(input())
l = n - s


def f(b):
    t = 0
    u = n
    while u != 0:
        t += u % b
        u = u // b
    return t


N = math.ceil(math.sqrt(n) + 2)
T = 10**12
if l < 0:
    print(-1)
    return
if l == 0:
    print(n + 1)
    return
for i in range(1, N):
    if l % i == 0:
        j = i + 1
        if f(j) == s and T > j:
            T = j
        elif f((l // i) + 1) == s and T > ((l // j) + 1):
            T = (l // i) + 1
if T == 10**12:
    print(-1)
    return
print(T)
