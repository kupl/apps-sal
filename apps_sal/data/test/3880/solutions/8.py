def main():
    n = int(input())
    l = list(map(int, input().split()))
    res = sum(map(abs, l))
    if not n & 1 and sum(x < 0 for x in l) & 1:
        res -= abs(min(l, key=abs)) * 2
    print(res)


def __starting_point():
    main()


__starting_point()
