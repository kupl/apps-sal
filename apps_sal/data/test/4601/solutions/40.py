def main():
    (n, k) = map(int, input().split(' '))
    h = list(map(int, input().split(' ')))
    h.sort(reverse=True)
    print(sum(h[k:]))


def __starting_point():
    main()


__starting_point()
