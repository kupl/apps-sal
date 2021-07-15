#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
BC= [list(map(int, input().split())) for _ in range(M)]

A.sort(reverse=True)

BC.sort(key=lambda x: x[1], reverse=True)
ans = 0
cnt = 0
while cnt < N:
    if len(BC) > 0 and A[0] < BC[0][1]:
        bc = BC.pop(0)
        ans += bc[1] * min(bc[0], N - cnt)
        cnt += bc[0]    
    else:
        ans += A.pop(0)
        cnt += 1

print(ans)




