def main():
    (w, h) = list(map(int, input().split()))
    a = [input() for i in range(h)]
    for i in range(w):
        b = [a[j][i] * 2 for j in range(h)]
        s = ''.join(b)
        print(s)
        print(s)


def __starting_point():
    main()


__starting_point()
