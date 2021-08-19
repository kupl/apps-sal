import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    (n, m) = map(int, input().split())
    price = [0] * m
    typesnum = [0] * m
    keybit = [0] * m
    for i in range(m):
        (price[i], typesnum[i]) = map(int, input().split())
        keybit[i] = sum(map(lambda x: 2 ** (int(x) - 1), input().split()))
    dp = [10 ** 9] * (1 << n)
    dp[0] = 0
    for bit in range(1 << n):
        for i in range(m):
            dp[bit | keybit[i]] = min(dp[bit | keybit[i]], dp[bit] + price[i])
    if dp[-1] == 10 ** 9:
        dp[-1] = -1
    print(dp[-1])


def __starting_point():
    main()


__starting_point()
