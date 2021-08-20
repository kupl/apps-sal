import sys
import math
from collections import defaultdict as dd
mod = 1000000007


def lcm(x, y):
    return x * y // math.gcd(x, y)


T = 1
for _ in range(T):
    (n, k) = list(map(int, input().split()))
    (a, b) = list(map(int, input().split()))
    p = []
    q = n * k
    (x, y) = (q, 0)
    for i in range(0, q, k):
        s1 = (i + b) % q
        s2 = (i - b) % q
        jmp = 0
        if s1 >= a:
            jmp = s1 - a
        else:
            jmp = q - a + s1
        if jmp == 0:
            jmp = q
        y = max(lcm(q, jmp) // jmp, y)
        x = min(lcm(q, jmp) // jmp, x)
        if s2 >= a:
            jmp = s2 - a
        else:
            jmp = q - a + s2
        if jmp == 0:
            jmp = q
        y = max(lcm(q, jmp) // jmp, y)
        x = min(lcm(q, jmp) // jmp, x)
    print(x, y)
