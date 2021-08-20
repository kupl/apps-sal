import numpy as np


def palace():
    N = int(input())
    (T, A) = np.array(input().split(), dtype='int')[:2]
    H = [int(i) for i in input().split()]
    min_dif = 10000
    place = 0
    for i in range(N):
        temp = T - H[i] * 0.006
        dif = abs(A - temp)
        if min_dif >= dif:
            min_dif = dif
            place = i + 1
    print(place)


palace()
