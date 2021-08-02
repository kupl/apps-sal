

def main():
    n, k = (int(x) for x in input().split())
    xs = [int(x) for x in input().split()]

    counter = 0
    arya = 0
    bran = 0

    for i, x in enumerate(xs):
        arya += x

        give = min(arya, 8)
        arya -= give
        bran += give

        if bran >= k:
            break

    if bran >= k:
        print(i + 1)
    else:
        print(-1)


def __starting_point():
    main()


__starting_point()
