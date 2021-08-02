import numpy as np

A, B, K = map(int, input().split())

if K > A:
    a = 0
    B = max(B - (K - A), 0)
else:
    a = A - K

print(a, B)
