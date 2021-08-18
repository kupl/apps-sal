mod = 10**9 + 7


def sum_interval_1d(N, X):
    X_ = [X[i + 1] - X[i] for i in range(N - 1)]
    coef = list(range(1, N))[::-1]
    ret = (X_[0] * coef[0]) % mod
    for i in range(1, N - 1):
        coef[i] = (coef[i] + coef[i - 1] - i) % mod
        ret = (ret + ((X_[i] * coef[i]) % mod)) % mod
    return ret


def solve():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    x_sum = sum_interval_1d(N, X)
    y_sum = sum_interval_1d(M, Y)
    ret = (x_sum * y_sum) % mod
    print(ret)


solve()
