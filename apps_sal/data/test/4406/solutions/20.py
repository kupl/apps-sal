import math


def inp(cast=int):
    return [cast(x) for x in input().split()]


printf = lambda s='', *args, **kwargs: print(str(s).format(*args), flush=True, **kwargs)
(n, k) = inp()
A = inp()
B = []
for a in A:
    if a in B:
        continue
    B = [a] + B
    if len(B) > k:
        B.pop()
print(len(B))
for b in B:
    print(b, end=' ')
