def main():
    n, k = map(int, input().split())
    hh = list(map(int, input().split()))
    s = sum(hh[:k])
    l = [s]
    for a, b in zip(hh, hh[k:]):
        s = s + b - a
        l.append(s)
    print(min(range(len(l)), key=l.__getitem__) + 1)


def __starting_point():
    main()
__starting_point()
