def __starting_point():
    n = int(input())
    a = [0 for i in range(n + 1)]
    i = 2
    sc = 1
    while i * i <= n:
        if a[i] == 0:
            a[i] = sc
            j = i * i
            while j <= n:
                a[j] = sc
                j += i
            sc += 1
        i += 1
    for i in range(2, n + 1):
        if a[i] == 0:
            a[i] = sc
            sc += 1
    print(' '.join(map(str, a[2:])))


__starting_point()
