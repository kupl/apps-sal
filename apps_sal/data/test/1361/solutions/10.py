def main():
    n = int(input())
    a = list(map(int, input().split()))
    min_max = 1000000
    max_diff = 0
    for i in range(1, n - 1):
        max_diff = 0
        c = a[:i] + a[i + 1:]
        for j in range(n - 2):
            max_diff = max(c[j + 1] - c[j], max_diff)
        min_max = min(max_diff, min_max)

    print(min_max)


def __starting_point():
    main()


__starting_point()
