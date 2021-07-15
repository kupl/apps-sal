#!/usr/bin/env python3

import heapq
#import
#import math
#import numpy as np
N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

A = [A[i] * (-1) for i in range(N)]
heapq.heapify(A)

for i in range(M):
    q = heapq.heappop(A)
    if q == 0:
        print((0))
        return
    heapq.heappush(A, int(q / 2))

print((sum(A) * (-1)))

