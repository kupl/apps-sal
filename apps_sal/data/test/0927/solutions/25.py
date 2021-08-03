import sys
input = sys.stdin.readline


def main():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))

    key = dict()
    if 1 in a:
        key[2] = 1
    for v in [5, 3, 2]:
        if v in a:
            key[5] = v
            break
    if 4 in a:
        key[4] = 4
    for v in [9, 6]:
        if v in a:
            key[6] = v
            break
    if 7 in a:
        key[3] = 7
    if 8 in a:
        key[7] = 8

    dp = [0] * (n + 1)

    for i in range(n):
        if i != 0 and dp[i] == 0:
            continue
        for k, v in list(key.items()):
            if i + k <= n:
                dp[i + k] = max(dp[i + k], 10 * dp[i] + v)
    print((dp[n]))


def __starting_point():
    main()


__starting_point()
