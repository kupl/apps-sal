def main():
    n = int(input())
    a = [int(x) for x in input().split()]

    idx = {}
    for i in range(len(a)):
        x = a[i]
        while x in idx:
            del idx[x]
            x *= 2
        # there is no any pair of equal number in idx
        # so every time when updating idx, i is the right place to record x
        idx[x] = i

    ans = list(sorted(idx.keys(), key=lambda x: idx[x]))
    print(len(ans))
    print(' '.join([str(x) for x in ans]))


def __starting_point():
    main()


__starting_point()
