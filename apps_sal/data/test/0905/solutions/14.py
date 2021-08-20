def __starting_point():
    (n, s) = [int(i) for i in input().split()]
    m = -1
    for i in range(n):
        (xi, yi) = [int(j) for j in input().split()]
        if xi < s:
            m = max(m, (100 - yi) % 100)
        if xi == s and yi == 0:
            m = max(m, 0)
    print(m)


__starting_point()
