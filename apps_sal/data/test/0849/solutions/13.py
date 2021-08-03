def main():
    l = [int(x) for x in input().split(' ')]
    r = (l[0] * l[3]) / (l[1] * l[2] + l[0] * l[3] - l[0] * l[2])
    print(r)


def __starting_point():
    main()


__starting_point()
