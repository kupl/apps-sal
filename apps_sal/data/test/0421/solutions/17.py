def main():
    res = t = 0
    for (r, l) in sorted((tuple(map(int, reversed(input().split()))) for _ in range(int(input())))):
        if t < l:
            t = r
            res += 1
    print(res)


def __starting_point():
    main()


__starting_point()
