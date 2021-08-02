from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())
c = []
a_list = []


def main():
    for i in range(m):
        a, b = map(int, stdin.readline().rstrip().split())
        a_list.append(a)
        c.append(sum(1 << j - 1 for j in list(map(int, stdin.readline().rstrip().split()))))

    inf = 10**10
    dp = [inf] * (1 << n)
    dp[0] = 0

    for i in range(1 << n):
        for A, C in zip(a_list, c):
            dp[C | i] = min(dp[C | i], dp[i] + A)

    if dp[-1] == inf:
        print(-1)
    else:
        print(dp[-1])


def __starting_point():
    main()


__starting_point()
