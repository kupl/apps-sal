def main():
    buf = input()
    T = int(buf)
    n = []
    k = []
    a = []
    for i in range(T):
        buf = input()
        buflist = buf.split()
        n.append(int(buflist[0]))
        k.append(int(buflist[1]))
        buf = input()
        buflist = buf.split()
        a.append(list(map(int, buflist)))
    for i in range(T):
        a[i].sort()
    for i in range(T):
        minimum_point = (a[i][0] + a[i][k[i]]) // 2
        minimum_value = max(abs(a[i][0] - minimum_point), abs(a[i][k[i]] - minimum_point))
        for j in range(1, n[i] - k[i]):
            window_minimum_point = (a[i][j] + a[i][k[i] + j]) // 2
            window_minimum_value = max(abs(a[i][j] - window_minimum_point), abs(a[i][k[i] + j] - window_minimum_point))
            if window_minimum_value < minimum_value:
                minimum_point = window_minimum_point
                minimum_value = window_minimum_value
        print(minimum_point)


def __starting_point():
    main()


__starting_point()
