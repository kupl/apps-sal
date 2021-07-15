#!/usr/bin/env python3

n = int(input())
x = [int(i) for i in input().split()]

S1, S3, L, R = 0, 0, -1, n
MaxS = 0
while L < R:
    if S1 == S3:
        MaxS = S1
        L += 1
        S1 += x[L]
    elif S1 > S3:
        R -= 1
        S3 += x[R]
    else:
        L += 1
        S1 += x[L]
print(MaxS)



