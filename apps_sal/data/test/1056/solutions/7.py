import sys


def read_ints():
    return [int(x) for x in sys.stdin.readline().split()]


def ind(i, j):
    return 10 * i + (j if i % 2 == 0 else 9 - j)


def read_field():
    field = [0] * 100
    for i in range(10):
        for j, h in enumerate(read_ints()[:10]):
            if h != 0:
                h = ind(i - h, j)
            else:
                h = ind(i, j)
            field[ind(i, j)] = h
    return field


def solve(field):
    dp = [1.0] * 100
    dp[0] = 0.0

    for _ in range(100):
        for i in range(1, 100):
            sum = 1.0
            for j in range(1, 7):
                if (i - j) >= 0:
                    sum += min(dp[i - j], dp[field[i - j]]) / 6
                else:
                    sum += dp[i] / 6
            dp[i] = sum

    return dp[99]


def main():
    field = read_field()
    result = solve(field)
    sys.stdout.write("{:.6f}\n".format(result))


def __starting_point():
    main()


__starting_point()
