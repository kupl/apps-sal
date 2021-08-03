import numpy as np


def f(nums, a):
    return 0 if nums.size <= 1 else (np.searchsorted(nums, a // nums, side='right').sum() - np.searchsorted(nums, int(pow(a, 1 / 2)), side='right')) // 2


N, K = map(int, input().split())
A = np.sort(list(map(int, input().split())))

p = np.sum(A > 0)
q = np.sum(A < 0)
Z = N - p - q
AP = A[-p:] if p > 0 else np.array([])
AN = A[:q] if q > 0 else np.array([])

b = (N - Z) * Z + Z * (Z - 1) // 2
a = p * q

if K <= a:
    x = AP[-1] * AN[0] - 1
    y = AP[0] * AN[-1]
    while y - x > 1:
        tmp = (y + x) // 2
        counter = np.searchsorted(AN, tmp // AP, side='right').sum()
        if counter < K:
            x = tmp
        else:
            y = tmp
    print(y)
elif K <= a + b:
    print(0)
else:
    x = 0
    y = 10**18
    K = K - a - b
    if q <= 1:
        while y - x > 1:
            tmp = (y + x) // 2
            if f(AP, tmp) < K:
                x = tmp
            else:
                y = tmp
        print(y)
        return

    AN = AN[::-1]
    AN = -AN

    if p <= 1:
        while y - x > 1:
            tmp = (y + x) // 2
            counter = f(AN, tmp)
            if counter < K:
                x = tmp
            else:
                y = tmp
        print(y)
        return

    while y - x > 1:
        tmp = (y + x) // 2
        if f(AP, tmp) + f(AN, tmp) < K:
            x = tmp
        else:
            y = tmp
    print(y)
