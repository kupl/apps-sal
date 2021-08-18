def works(X, N, M, K):
    res = 0
    n = 1
    div = X / M
    while n < div:
        res += M
        n += 1
    while n < N + 1:
        res += (X - 1) // n
        n += 1
    return res


def solve():
    N, M, K = [int(s) for s in input().split()]
    left = 1
    right = K + 1
    while right - left > 1:
        middle = (left + right) // 2
        if works(middle, N, M, K) < K:
            left = middle
        else:
            right = middle
    return left


print(solve())
