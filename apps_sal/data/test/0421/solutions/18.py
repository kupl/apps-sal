def main():
    res = t = 0
    for l, r in sorted((tuple(map(int, input().split())) for _ in range(int(input()))), key=lambda e: e[1]):
        if t < l:
            t = r
            res += 1
    print(res)


def __starting_point():
    main()


__starting_point()
