def main():
    (n, k) = list(map(int, input().split()))
    d = set()
    for i in range(k):
        input()
        d.update(list(map(int, input().split())))
    print(n - len(d))


def __starting_point():
    main()


__starting_point()
