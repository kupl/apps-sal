import io
import os

q = int(input())

for i in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    mn, mx = 10 ** 18, 0
    for c in a:
        if c < mn:
            mn = c
        if c > mx:
            mx = c
        d[c] = d.get(c, 0) + 1

    s = mn * mx
    f = True
    for c in d:
        if not(d[c] % 2 == 0 and s % c == 0 and d.get(s // c, 0) == d[c]):
            f = False
            print("NO")
            break
    if f:
        print("YES")
