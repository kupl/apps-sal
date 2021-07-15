import math

N = 5
ARR = [2, 4, 4, 0, 2]

N = 7
ARR = [6, 4, 0, 2, 4, 0, 2]
#
# N = 8
# ARR = [7, 5, 1, 1, 7, 3, 5, 3]
#
N = int(input())
ARR = list(map(int, input().split()))


def calculate(n, arr):
    if n % 2 == 0:
        n = n // 2
        start = 1
        finalResult = pow(2, n, 1000000000 + 7)
    else:
        n = n // 2 + 1
        start = 0
        finalResult = pow(2, (n - 1), 1000000000 + 7)

    result = {}
    for i in range(n):
        index = start + 2 * i
        if index == 0:
            result.__setitem__(0, 1)
        else:
            result.__setitem__(index, 2)

    isOk = True
    for i in range(len(arr)):
        if result.get(arr[i]) == None:
            isOk = False
            break

        if result.get(arr[i]) == 0:
            isOk = False
            break

        result.__setitem__(arr[i], result.get(arr[i])-1)

    if isOk == False:
        print((0))
        return

    if sum(result.values()) == 0:
        print(finalResult)
    else:
        print((0))


calculate(N, ARR)

