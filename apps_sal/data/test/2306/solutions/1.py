import sys
input = sys.stdin.readline


def main():
    n = int(input())
    t = list(map(int, input().split()))
    v = list(map(int, input().split()))
    length = sum(t) * 2
    dp = [0] * (length + 1)
    border = v[0]
    count = t[0] * 2
    index = 0
    for i in range(length):
        dp[i + 1] = min(dp[i] + 0.5, border)
        count -= 1
        if i == length - 1:
            break
        if count == 0:
            index += 1
            border = v[index]
            count = t[index] * 2
    dp[length] = 0
    border = v[n - 1]
    count = t[n - 1] * 2
    index = n - 1
    for i in range(length, 0, -1):
        dp[i - 1] = min([dp[i] + 0.5, border, dp[i - 1]])
        count -= 1
        if i == 0:
            break
        if count == 0:
            index -= 1
            border = v[index]
            count = t[index] * 2
    ans = 0
    for i in range(length):
        ans += (dp[i] + dp[i + 1]) / 4
    print(ans)


def __starting_point():
    main()


__starting_point()
