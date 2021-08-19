from functools import reduce
from fractions import gcd


def ll():
    return list(map(int, input().split()))


def find_gcd(list):
    x = reduce(gcd, list)
    return x


testcases = 1
for _ in range(testcases):
    [n] = ll()
    a = ll()
    amax = max(a)
    l = []
    ans = 0
    for x in range(n):
        if not amax == a[x]:
            l.append(amax - a[x])
    h = find_gcd(l)
    for x in range(n):
        if not amax == a[x]:
            ans += (amax - a[x]) // h
    print(ans, h)
