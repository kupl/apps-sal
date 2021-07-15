#!/usr/bin/env python3

#import
#import math
#import numpy as np
N, K = list(map(int, input().split()))
R, S, P = list(map(int, input().split()))
T = list(input())

ans = 0

for i in range(K):
    last = ""
    for j in range(i, N, K):
        if T[j] == last:
            last = ""
            continue

        if T[j] == "r":
            ans += P
        elif T[j] == "s":
            ans += R
        else:
            ans += S

        last = T[j]

print(ans)

