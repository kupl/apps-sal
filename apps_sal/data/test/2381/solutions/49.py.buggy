#!/usr/bin/env python3
from functools import reduce

mod = 10**9 + 7
n, k, *a = list(map(int, open(0).read().split()))
a.sort(key=lambda x: abs(x))
ans = reduce(lambda a, b: (a * b) % mod, a[-k:])

c = a[-k:]
j = sum(i < 0 for i in c) % 2
if j:
    c = a[-k:]
    neg = [i for i in c if i < 0]
    pos = [i for i in c if i > 0]
    b = sorted(a[:n - k])
    if b == []:
        print(ans)
        return
    if neg == []:
        if pos[0] * b[0] < 0:
            ans = ans * pow(pos[0], mod - 2, mod) * b[0] % mod
        else:
            ans = reduce(lambda a, b: (a * b) % mod, a[:k])
    elif pos == []:
        if neg[0] * b[-1] < 0:
            ans = ans * pow(neg[0], mod - 2, mod) * b[-1] % mod
        else:
            ans = reduce(lambda a, b: (a * b) % mod, a[:k])
    elif pos[0] * b[-1] < neg[0] * b[0] and pos[0] * b[0] < 0:
        ans = ans * pow(pos[0], mod - 2, mod) * b[0] % mod
    elif 0 > b[-1] * neg[0]:
        ans = ans * pow(neg[0], mod - 2, mod) * b[-1] % mod
    else:
        ans = reduce(lambda a, b: (a * b) % mod, a[:k])
print(ans)
