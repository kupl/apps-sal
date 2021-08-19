# ABC136 B

import math
N = int(input())
digit = int(math.log10(N)) + 1
S = 0
if digit % 2 == 0:
    for i in range(1, int(digit / 2) + 1):
        S += pow(10, 2 * i - 1) - pow(10, 2 * i - 2)
    print(S)
if digit % 2 == 1:
    for i in range(1, int((digit + 1) / 2)):
        S += pow(10, 2 * i - 1) - pow(10, 2 * i - 2)
    S += N - pow(10, digit - 1) + 1
    print(S)
