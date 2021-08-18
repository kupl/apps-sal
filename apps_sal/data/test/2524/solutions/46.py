import math
import numpy as np

N = 10
ARR = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

N = 10
ARR = [3, 14, 159, 2653, 58979, 323846, 2643383, 27950288, 419716939, 9375105820]


N = int(input())
ARR = list(map(int, input().split()))


def calculate(n, arr):
    if max(arr) == 0:
        mathNum = 1
    else:
        mathNum = math.ceil(math.log(max(arr), 2))

    oneArray = [0] * mathNum
    zeroArray = [0] * mathNum

    result = 0
    arr = np.array(arr)
    for i in range(mathNum):
        s = (arr >> i) & 1

        oneCount = np.count_nonzero(s)
        zeroCount = n - oneCount
        oneArray[i] = oneCount
        zeroArray[i] = zeroCount

    for i in range(mathNum):
        result += (2 ** i) * (oneArray[i] * zeroArray[i])

    print(result % (10 ** 9 + 7))


calculate(N, ARR)
