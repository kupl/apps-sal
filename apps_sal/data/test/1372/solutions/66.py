import sys
read = sys.stdin.read


def main():
    (h, n) = map(int, input().split())
    m = map(int, read().split())
    mm = zip(m, m)
    large_num = 10 ** 9
    dp = [large_num] * (h + 10 ** 4 + 1)
    dp[0] = 0
    for (a, b) in mm:
        for i1 in range(h + 1):
            if dp[i1 + a] > dp[i1] + b:
                dp[i1 + a] = dp[i1] + b
    r = min(dp[h:])
    print(r)


def __starting_point():
    main()


__starting_point()
