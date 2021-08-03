import sys
input = sys.stdin.readline


def main():
    n, m = list(map(int, input().split()))
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    X = [x[i + 1] - x[i] for i in range(n - 1)]
    Y = [y[i + 1] - y[i] for i in range(m - 1)]

    mod = pow(10, 9) + 7
    for i in range(n - 1):
        X[i] = X[i] * (n - i - 1) * (i + 1) % mod

    sum_x = sum(X) % mod

    for i in range(m - 1):
        Y[i] = Y[i] * (m - i - 1) * (i + 1) % mod

    sum_y = sum(Y) % mod

    ans = sum_x * sum_y % mod

    print(ans)


def __starting_point():
    main()


__starting_point()
