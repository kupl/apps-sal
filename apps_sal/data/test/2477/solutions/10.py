import math

N, K = (int(a) for a in input().split())
A = [int(a) for a in input().split()]


def isOK(X):
    cutcount = 0
    for i in range(N):
        cutcount += math.ceil(A[i] / X) - 1
    if cutcount <= K:
        return True
    else:
        return False


def binary_search():
    left = 0
    right = max(A) + 1

    while (right - left) > 1:
        mid = left + (right - left) // 2
        if (isOK(mid)):
            right = mid
        else:
            left = mid

    return right


print(binary_search())
