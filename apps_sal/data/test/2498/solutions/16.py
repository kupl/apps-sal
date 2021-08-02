import math
import numpy as np
N, M = map(int, input().split())
A = list(map(int, input().split()))
c = 1
test = A[0]
l = 0

while test % 2 == 0:
    test = test // 2
    c *= 2


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


for i in np.arange(N - 1):
    if A[i + 1] % c != 0:
        print(0)
        l = 1
        break
    elif A[i + 1] % (c * 2) == 0:
        print(0)
        l = 1
        break
    else:
        k = A[i + 1] // c
        test = lcm_base(test, k)
if l == 0:
    k = test * c // 2
    print(M // k // 2 + M // k % 2)
