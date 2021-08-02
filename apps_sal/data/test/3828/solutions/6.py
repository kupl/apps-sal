def main():
    n = int(input())
    l = [n] * (n + 1)
    for a in map(int, input().split()):
        l[a] = l[a - 1] - 1
    print(min(l))


def __starting_point():
    main()


__starting_point()
