def main():
    input()
    x, l = 0, [0]
    for a in map(int, input().split()):
        x ^= a
        l.append(x)
    print(max(a ^ l[j] for i, a in enumerate(l) for j in range(i)))


def __starting_point():
    main()


__starting_point()
