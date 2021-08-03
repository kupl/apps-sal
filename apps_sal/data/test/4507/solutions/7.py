from collections import defaultdict


def buy(k, sums, offset, discounts):
    return sums[offset + k] - sums[offset + discounts[k]]


def main():
    n, m, k = list(map(int, input().split()))
    prices = sorted(list(map(int, input().split())))[:k]
    sums = [0] * (k + 1)
    for i in range(1, k + 1):
        sums[i] = sums[i - 1] + prices[i - 1]

    discounts = defaultdict(int)
    for _ in range(m):
        x, y = tuple(map(int, input().split()))
        discounts[x] = max(discounts[x], y)

    d = [0] * (k + 1)

    for i in range(1, k + 1):
        d[i] = buy(i, sums, 0, discounts)

        for j in range(1, i + 1):
            d[i] = min(d[i], d[j] + buy(i - j, sums, j, discounts))

    print(d[k])


def __starting_point():
    main()


__starting_point()
