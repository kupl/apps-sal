def sum_n(n):
    return n * (n + 1) // 2


def main():
    mode = "filee"
    if mode == "file": f = open("test.txt", "r")
    get = lambda: [int(x) for x in (f.readline() if mode == "file" else input()).split()]
    [t] = get()
    for z in range(t):
        [n] = get()
        hold = sum_n(n)
        j = 1
        while j <= n:
            j = j << 1
            hold -= j
        print(hold)

    if mode == "file": f.close()


def __starting_point():
    main()


__starting_point()
