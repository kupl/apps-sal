def main():
    n = int(input())
    l = [-2] * 1001
    for x in map(int, input().split()):
        l[x] += 2
    print(('NO', 'YES')[max(l) < n])


def __starting_point():
    main()


__starting_point()
