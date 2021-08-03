#!/usr/bin/env python3

N, H = list(map(int, input().split()))

A = []
B = []

for i in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)

A = sorted(A)[::-1]
B = sorted(B)[::-1]

ret = 0
if B[0] < A[0]:
    if H % A[0] == 0:
        ret = H // A[0]
    else:
        ret = H // A[0] + 1
    H = 0
else:
    for b in B:
        if b < A[0]:
            if H % A[0] == 0:
                ret += H // A[0]
            else:
                ret += H // A[0] + 1
            H = 0
            break
        else:
            ret += 1
            H -= b

        if H <= 0:
            break

    if H > 0:
        if H % A[0] == 0:
            ret += H // A[0]
        else:
            ret += H // A[0] + 1


print(ret)
