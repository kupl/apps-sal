def main():
    n, aa, bb = int(input()), [], []
    for _ in range(n):
        a, b = input().split()
        aa.append(a)
        bb.append(b)
    print(n - len({i for i, a in enumerate(aa) for j, b in enumerate(bb) if i != j and a == b}))


def __starting_point():
    main()

__starting_point()
