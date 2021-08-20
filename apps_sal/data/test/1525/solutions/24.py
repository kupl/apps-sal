def main():
    (h, w, k) = list(map(int, input().split()))
    bf = [0] * (w + 2)
    nx = [0] * (w + 2)
    bf[1] = 1
    c = [1, 1, 2, 3, 5, 8, 13, 21]
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            nx[j] = c[j - 1] * c[w - j] * bf[j] + c[j - 1] * c[w - j - 1] * bf[j + 1] + c[j - 2] * c[w - j] * bf[j - 1]
        bf = nx
        nx = [0] * (w + 2)
    print(bf[k] % (10 ** 9 + 7))


def __starting_point():
    main()


__starting_point()
