import sys


def main():
    s = input()
    n = len(s)
    lim = 243
    ar = [int(c) for c in s]
    dp = [0] * (n + lim + 3)
    for i in range(n - 1, -1, -1):
        x = 0
        k = 1 if ar[i] == 0 else lim
        for j in range(k):
            if i + j == n:
                break
            x = (x * 10 + ar[i + j]) % 3
            dp[i] = max(dp[i], dp[i + j + 1] + (x == 0))
    print(dp[0])


def __starting_point():
    main()


__starting_point()
