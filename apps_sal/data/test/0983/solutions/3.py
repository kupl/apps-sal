def main():
    n, p, q, r = list(map(int, input().split()))
    a = list(map(int, input().split()))
    dp = [float('-inf') for _ in range(n)]
    dp[-1] = r * a[-1]

    for i in range(n - 2, -1, -1):
        dp[i] = max(r * a[i], dp[i + 1])

    dp2 = [float('-inf') for _ in range(n)]
    dp2[-1] = (q + r) * a[-1]
    for i in range(n - 2, -1, -1):
        dp2[i] = max(q * a[i] + dp[i], dp2[i + 1])

    dp3 = [float('-inf') for _ in range(n)]
    dp3[-1] = (p + q + r) * a[-1]
    for i in range(n - 2, -1, -1):
        dp3[i] = max(p * a[i] + dp2[i], dp3[i + 1])

    print(dp3[0])

main()

