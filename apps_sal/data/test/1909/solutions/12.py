def main():
    n, k = list(map(int, input().split()))
    aa = list(map(int, input().split()))
    res = [sum(aa[i::k]) for i in range(k)]
    print(min(list(range(k)), key=res.__getitem__) + 1)


def __starting_point():
    main()

__starting_point()
