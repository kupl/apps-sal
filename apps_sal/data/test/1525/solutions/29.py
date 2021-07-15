def fib(n):
    a = 1
    b = 0
    i = 0
    while i < n:
        i += 1
        c = a + b
        yield c
        a = b
        b = c


def main():
    h, w, k = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    
    dp = [[0] * (w + 2) for _ in range(h + 1)]
    dp[0][1] = 1
    c = [i for i in fib(w + 1)]

    for i in range(1, h + 1):
        for j in range(1, w + 1):
            x = c[j - 1] * c[w - j]
            y = c[j - 1] * c[w - j - 1]
            z = c[j - 2] * c[w - j]

            dp[i][j] = (x * dp[i - 1][j] + y * dp[i - 1][j + 1] + z * dp[i - 1][j - 1]) % mod

    print((dp[h][k]))


def __starting_point():
    main()

__starting_point()
