#!/usr/bin/env python3

import sys
[n, k] = list(map(int, input().strip().split()))
pis = list(map(int, input().strip().split()))

if k == 1:
    print(' '.join(map(str, pis)))
    return


N = 256
gamma = [-1 for _ in range(N)]
done = [False for _ in range(N)]
revdone = [False for _ in range(N)]
notset = 256
pends = {}


def get_bounds(i):
    try:
        l = N - 1 - revdone.index(True, N - 1 - i) + 1
    except ValueError:
        l = 0
    try:
        r = done.index(True, i) - 1
    except ValueError:
        r = N - 1
    return l, r


def set_gamma(l, r, v):
    for i in range(l, r + 1):
        gamma[i] = v
        done[i] = True
        revdone[N - 1 - i] = True


for p in pis:
    if not done[p]:
        lb, rb = get_bounds(p)
        if (lb > 0) and ((lb - 1) in pends) and (lb - 1 + pends[lb - 1] >= p):
            l = lb
            r = p
            set_gamma(l, r, gamma[lb - 1])
            if r - l + 1 < pends[lb - 1]:
                pends[r] = pends[lb - 1] - (r - l + 1)
            del pends[lb - 1]
        else:
            l = max(p - k + 1, lb)
            r = p
            set_gamma(l, r, l)
            if r - l + 1 < k:
                pends[p] = k - (r - l + 1)
        notset -= r - l + 1
        if notset == 0:
            break

if notset > 0:
    for i in range(N):
        if gamma[i] < 0:
            l, r = get_bounds(i)
            set_gamma(l, min(l + k - 1, r), l)

print(' '.join(str(gamma[p]) for p in pis))
