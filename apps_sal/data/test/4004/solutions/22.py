def main():

    n = int(input())
    ints = list(map(int, input().split()))

    ints = sorted(list(set(ints)))

    if len(ints) > 3:
        print(-1)
        return
    if len(ints) == 3:
        if (ints[1] - ints[0]) == (ints[2] - ints[1]):
            print(ints[1] - ints[0])
        else:
            print(-1)
        return
    if len(ints) == 2:
        if (ints[0] + ints[1]) % 2 == 0:
            print((ints[0] + ints[1]) // 2 - ints[0])
        else:
            print(ints[1] - ints[0])
        return
    print(0)
    return

def __starting_point():
    main()
__starting_point()
