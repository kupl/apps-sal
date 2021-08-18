

import math


def cin():
    return list(map(int, input().split()))


count = 0
N = cin()[0]

for A in range(1, N + 1):
    B = math.floor(N / A)
    C = N % A

    if B != 0 and C != 0:
        count += B
    elif B != 0 and C == 0:
        count += B - 1

print(count)
