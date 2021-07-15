#!/usr/bin/env python3

#import
#import math
#import numpy as np
N, M = list(map(int, input().split()))

K = {i: [] for i in range(M)}
for i in range(M):
    t = list(map(int, input().split()))
    for j in range(1, len(t)):
        K[i].append(t[j] - 1)

P = list(map(int, input().split()))

ans = 0

for i in range(2 ** N):
    switch = [False] * N
    for j in range(N):
        if (i >> j) & 1:
            switch[j] = True

    isok = True
    for m in range(M):
        t = 0
        for k in K[m]:
            if switch[k]:
                t += 1

        if (t % 2) != P[m]:
            isok = False

    if isok:
        ans += 1

print(ans)



