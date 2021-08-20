from math import ceil
(n, s) = list(map(int, input().split()))
peb = list(map(int, input().split()))
d = 0
for p in peb:
    d += ceil(p / s)
print(ceil(d / 2))
