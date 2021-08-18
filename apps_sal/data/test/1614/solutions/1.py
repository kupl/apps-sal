
def main():
    n, h = map(int, input().split())
    w = 0
    for i in input().split():
        if int(i) > h:
            w += 2
        else:
            w += 1
    print(w)


def __starting_point():
    main()


__starting_point()
