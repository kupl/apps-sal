def main():
    n, k = map(int, input().split())
    l = list(range(1, n * k + 1))
    aa = list(map(int, input().split()))
    for a in aa:
        l[a - 1] = False
    l = list(filter(None, l))
    n -= 1
    for i, a in enumerate(aa):
        print(a, *l[i * n:(i + 1) * n])


def __starting_point():
    main()


__starting_point()
