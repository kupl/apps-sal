def main():
    n, l = int(input()), [(0, "")]
    for c in map(int, input().split()):
        s = input()
        l = [(x + dx, b) for dx, b in ((0, s), (c, s[::-1])) for x, a in l if a <= b]
        l.sort()
        for i in range(len(l) - 1, 0, -1):
            for j in range(i):
                if l[i][1] >= l[j][1]:
                    del l[i]
                    break
    print(min(l)[0] if l else -1)


def __starting_point():
    main()


__starting_point()
