import math


def __starting_point():
    n, k = list(map(int, input().split()))
    A = list(map(int, input().split()))
    x = int((-1 + math.sqrt(1 + 8 * k)) / 2)
    if k == (1 + x) * x // 2:
        print(A[x - 1])
    else:
        print(A[k - (1 + x) * x // 2 - 1])


__starting_point()
