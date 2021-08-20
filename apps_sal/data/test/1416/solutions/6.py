def main():
    (n, w) = list(map(int, input().split()))
    a = sorted(map(int, input().split()))
    print(min(w, min(a[0], a[n] * 0.5) * 3 * n))


def __starting_point():
    main()


__starting_point()
