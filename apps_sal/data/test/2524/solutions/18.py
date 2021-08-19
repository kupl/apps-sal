import math
import numpy as np
N = int(input())
ARR = list(map(int, input().split()))


def calculate(n, arr):
    maxValue = max(arr)
    if maxValue == 0:
        maxNum = 1
    else:
        maxNum = math.ceil(math.log(maxValue, 2))
    arr = np.array(arr)
    oneArray = [0] * (maxNum + 1)
    zeroArray = [0] * (maxNum + 1)
    for i in range(maxNum + 1):
        s = arr >> i & 1
        a = np.count_nonzero(s)
        oneArray[i] = a
        zeroArray[i] = n - a
    finalResult = 0
    for i in range(maxNum + 1):
        finalResult += 2 ** i * oneArray[i] * zeroArray[i]
    print(finalResult % (10 ** 9 + 7))


calculate(N, ARR)
