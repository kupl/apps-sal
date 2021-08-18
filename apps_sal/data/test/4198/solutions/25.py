
import sys
from math import ceil
A, B, X = list(map(int, input().split()))


def calc(N, L_N):
    return A * N + B * L_N


l = 0
r = 10 ** 9 + 1

while r - l > 1:
    c = (r + l) // 2
    if calc(c, len(str(c))) <= X:
        l = c
    else:
        r = c

print(l)
