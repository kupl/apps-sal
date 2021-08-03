def main():
    k, n = map(int, input().split())
    a = [int(v) for v in input().split()]
    distances = []
    for i in range(1, len(a)):
        distances.append((a[i] - a[i - 1]))
    distances.append((k + a[0]) - a[-1])
    maximum = max(distances)
    return k - maximum


def __starting_point():
    print(main())


__starting_point()
