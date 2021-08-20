def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    total = 0
    for i in range(1, n + 1):
        if a[i - 1] > a[i]:
            total += a[i] * (a[i - 1] - a[i])
        elif a[i - 1] < a[i]:
            total += (a[i] - a[i - 1]) * (n - a[i] + 1)
    print(total)


def __starting_point():
    main()


__starting_point()
