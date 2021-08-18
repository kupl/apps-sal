

import itertools


def sieve(x):
    p = []
    b = [1] * (x + 1)
    for i in range(2, x + 1):
        if b[i]:
            p += [i]
            for j in range(2 * i, x + 1, i):
                b[j] = 0
    return p


p = sieve(10**5)


s = set(i for i in p if i < 5 * 10**4)
l = [0] * (10**5)
for i in p[1:]:
    if i // 2 + 1 in s:
        l[i] = 1
S = list(itertools.accumulate(l))


Q = int(input())
for _ in range(Q):
    l, r = list(map(int, input().split()))
    print((S[r] - S[l - 1]))
