def main():
    N, T = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(N)]

    dp = [-1] * (T + 3000)
    dp[0] = 0
    c = 0
    for a, b in sorted(AB):
        for j in range(c, -1, -1):
            if dp[j] == -1:
                continue
            t = dp[j] + b
            if dp[j + a] < t:
                dp[j + a] = t
        c = min(c + a, T - 1)
    print((max(dp)))


main()
