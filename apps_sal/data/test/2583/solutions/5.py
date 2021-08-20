from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict as dd, Counter
from math import ceil
from math import gcd
import sys
INF = 10 ** 20
MOD = 10 ** 9 + 7


def I():
    return list(map(int, input().split()))


def solve():
    (n,) = I()
    f = 'FastestFinger'
    a = 'Ashishgup'
    if n == 1:
        print(f)
        return
    if n == 2:
        print(a)
        return
    if not n & n - 1:
        print(f)
        return
    lala = 0
    if n % 2:
        print(a)
        return
    count = 0
    while n % 2 == 0:
        n //= 2
        lala += 1
    for i in range(3, int(n ** 0.5) + 10, 2):
        while n % i == 0:
            count += 1
            n //= i
    if n > 1:
        count += 1
    if lala == 1 and count == 1:
        print(f)
        return
    if count % 2:
        print(a)
    else:
        print(a)


(t,) = I()
while t:
    t -= 1
    solve()
'\nFacts and Data representation\n'
