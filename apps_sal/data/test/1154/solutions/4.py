#!/usr/bin/env python3

N, H, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

result = 0
fill = 0
p = 0

while p < len(A) or fill != 0:
    while p < len(A) and fill + A[p] <= H:
        fill += A[p]
        p += 1

    if p < len(A):
        need = A[p] - (H - fill)
    else:
        need = fill

    time = (need + K - 1) // K
    fill = max(0, fill - time * K)
    result += time

print(result)

