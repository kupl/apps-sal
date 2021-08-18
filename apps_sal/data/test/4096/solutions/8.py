

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    c = a.copy()
    for i in range(1, n):
        c[i] = c[i] + c[i - 1]

    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[0][i] = max(0, c[i] - (1 + i) * i // 2)
        if dp[0][i] >= m:
            print(1)
            return

    for i in range(1, n):
        for j in range(i, n):
            for k in range(i - 1, j):
                num = j - k - 1
                dp[i][j] = max(dp[i][j], dp[i - 1][k] + c[j] - c[k] - (1 + num) * num // 2)
            if dp[i][j] >= m:
                print(i + 1)
                return

    print(-1)


def __starting_point():
    main()


__starting_point()
