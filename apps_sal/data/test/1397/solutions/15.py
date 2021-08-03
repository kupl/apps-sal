def main():
    n, m = map(int, input().split())
    l = [True] * (n + 1)
    l[0] = False
    for _ in range(m):
        a, b = map(int, input().split())
        l[a] = l[b] = False
    center = l.index(True)
    print(n - 1)
    for i in range(1, center):
        print(center, i)
    for i in range(center + 1, n + 1):
        print(center, i)


def __starting_point():
    main()


__starting_point()
