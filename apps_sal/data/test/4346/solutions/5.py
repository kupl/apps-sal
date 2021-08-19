def main():
    t = int(input())
    for _ in range(t):
        (L, v, l, r) = list(map(int, input().split()))
        numbefore = (l - 1) // v
        numduring = r // v
        numafter = L // v
        print(numafter - (numduring - numbefore))


def __starting_point():
    main()


__starting_point()
