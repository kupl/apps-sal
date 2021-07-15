3
# coding: utf-8

import sys

N, K = (int(x) for x in input().split())
A = [int(x) for x in input().split()]

if N <= K:
    print(1)
    return

N -= K

ret = 1
ret += N // (K-1)
if N % (K-1)  != 0:
    ret += 1

print(ret)
