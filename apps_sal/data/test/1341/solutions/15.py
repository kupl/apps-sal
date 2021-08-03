def main():
    way = input()
    i = 0
    for c in input():
        if c == way[i]:
            i += 1
    print(i + 1)


def __starting_point():
    main()


__starting_point()
