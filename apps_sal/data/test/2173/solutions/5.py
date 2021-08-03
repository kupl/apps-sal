def main():
    n = int(input())
    aa = list(map(int, input().split()))
    idx = sorted(list(range(n)), key=aa.__getitem__)
    b = 0
    for i in idx:
        aa[i] = b = max(b + 1, aa[i])
    print(' '.join(map(str, aa)))


def __starting_point():
    main()


__starting_point()
