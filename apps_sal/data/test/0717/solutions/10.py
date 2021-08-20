def main():
    n = int(input())
    t = -1
    for i in range(n):
        (si, di) = list(map(int, input().split()))
        if t < si:
            t = si
        else:
            t = ((t - si) // di + 1) * di + si
    print(t)


def __starting_point():
    main()


__starting_point()
