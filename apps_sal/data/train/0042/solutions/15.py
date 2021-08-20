from collections import defaultdict
from math import log2


def zeros(n):
    return n - int(log2(n)) - 1


def binary(n):
    s = ''
    while n > 0:
        s = str(n & 1) + s
        n = n // 2
    return s


t = int(input())
d = defaultdict(list)
for i in range(1, 2 * 10 ** 5 + 1):
    z = zeros(i)
    d[z].append(i)
for _ in range(t):
    s = input()
    n = len(s)
    zs = [0] * n
    z = 0
    for i in reversed(list(range(n))):
        if s[i] == '0':
            z += 1
        else:
            z = 0
        zs[i] = z
    total = 0
    for i in range(n):
        z = zs[i]
        candidates = d[z]
        j = i + z
        for c in candidates:
            cS = binary(c)
            cSL = len(cS)
            jEnd = j + cSL
            if jEnd > n:
                continue
            if s[j:jEnd] == cS:
                total += 1
    print(total)
