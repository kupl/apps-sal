def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted([(j, i) for (i, j) in enumerate(a)])[::-1]
    dp = [0]
    for i in range(n):
        dp2 = [0] * (i + 2)
        (A, p) = a[i]
        for j in range(i + 1):
            right = n - i - 1 + j
            dp2[j] = max(dp2[j], dp[j] + abs(p - right) * A)
            dp2[j + 1] = max(dp2[j + 1], dp[j] + abs(p - j) * A)
        dp = dp2
    print(max(dp2))


main()
