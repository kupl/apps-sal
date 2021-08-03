from math import ceil
n, a, b = map(int, input().split())

c = int(n * (a / (a + b)))
d = n - c
cc = ceil(n * (a / (a + b)))
dd = n - cc
opts = []
if c != 0 and d != 0:
    opts.append(min(a // c, b // d))
if cc != 0 and dd != 0:
    opts.append(min(a // cc, b // dd))
print(max(opts))
