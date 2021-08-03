INF = 1e10
max_n = 50
max_k = 2000


def main():
    n, s, k = map(int, input().split())
    s -= 1
    buf = [''] * (max_n + 1)
    dp = [[0 for i in range(max_n + 1)] for j in range(max_k + 1)]
    r = list(map(int, input().split()))
    c = input()
    answer = INF
    for i in range(len(c)):
        buf[i] = c[i]
    for i in range(k, -1, -1):
        for j in range(n):
            dp[i][j] = INF
    for j in range(n):
        value = abs(j - s)
        if k - r[j] <= 0:
            answer = min(answer, value)
        else:
            dp[k - r[j]][j] = value
    for i in range(k, 0, -1):
        for j in range(n):
            if dp[i][j] < INF:
                for l in range(n):
                    if buf[j] != buf[l] and r[j] < r[l]:
                        value = dp[i][j] + abs(j - l)
                        if i - r[l] <= 0:
                            answer = min(answer, value)
                        else:
                            dp[i - r[l]][l] = min(dp[i - r[l]][l], value)
    if answer == INF:
        print(-1)
        return
    print(answer)


def __starting_point():
    main()


__starting_point()
