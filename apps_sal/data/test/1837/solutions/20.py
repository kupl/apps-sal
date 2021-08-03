def main():
    n = int(input())
    v = list(map(int, input().split()))
    a, c1, ok = 0, 0, 0
    for i in range(n):
        if (v[i] == i):
            c1 = c1 + 1
        elif (v[v[i]] == i):
            ok = 1
    if (c1 == n):
        print(c1)
    elif (ok):
        print(c1 + 2)
    else:
        print(c1 + 1)


def __starting_point():
    main()


__starting_point()
