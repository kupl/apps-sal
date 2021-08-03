def readints():
    return [int(x) for x in input().strip().split()]


def main():
    n, m = readints()
    p = readints()
    sums = {}

    pivot = p.index(m)

    diff = 0
    sums[0] = 1
    for i in range(pivot - 1, -1, -1):
        if p[i] > m:
            diff += 1
        else:
            diff -= 1
        sums.setdefault(diff, 0)
        sums[diff] += 1

    ans = 0
    diff = 0
    for i in range(pivot, n):
        if p[i] > m:
            diff += 1

        if p[i] < m:
            diff -= 1

        ans += sums.get(-diff, 0) + sums.get(1 - diff, 0)

    print(ans)


def __starting_point():
    main()


__starting_point()
