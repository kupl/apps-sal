def s(a):
    k = len(a)
    for i in range(k - 1):
        for j in range(i, k - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def main():
    n = int(input())
    if n <= 2:
        v = [-1]
    else:
        v = [int(i) for i in range(n, 0, -1)]
    print(*v, sep=' ')


def __starting_point():
    main()


__starting_point()
