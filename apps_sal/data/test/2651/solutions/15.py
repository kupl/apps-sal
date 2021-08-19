import sys
input = sys.stdin.readline


def main():
    (n, m) = list(map(int, input().split()))
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    X = [x[i + 1] - x[i] for i in range(n - 1)]
    Y = [y[i + 1] - y[i] for i in range(m - 1)]
    mod = pow(10, 9) + 7
    for i in range(n - 1):
        X[i] = X[i] * (n - i - 1) * (i + 1) % mod
    sum_x = sum(X) % mod
    ans = 0
    for j in range(m - 1):
        ans += sum_x * Y[j] * (m - j - 1) * (j + 1) % mod
        ans %= mod
    print(ans)


def __starting_point():
    main()


__starting_point()
