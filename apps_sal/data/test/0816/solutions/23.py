def main():
    (n, x) = list(map(int, input().split()))
    (l, res) = ([0] * 131073, 0)
    for a in map(int, input().split()):
        res += l[a ^ x]
        l[a] += 1
    print(res)


def __starting_point():
    main()


__starting_point()
