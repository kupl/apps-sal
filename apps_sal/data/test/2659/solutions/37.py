# -*- coding: utf-8 -*-
k = int(input())


def snuke(n):
    s = 0
    for _ in str(n):
        s += int(_)
    return n / s


n = 1
d = 0
for _ in range(k):
    print(n)
    if snuke(n + 10**d) > snuke(n + 10**(d + 1)):
        d += 1
    n += 10**d

