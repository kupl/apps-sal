def __starting_point():
    n = int(input())
    a = [0 for i in range(n + 1)]
    m = 1
    for i in range(2, len(a)):
        if a[i] == 0:
            a[i] = m
            for j in range(i * i, len(a), i):
                a[j] = m
            m += 1
    print(" ".join([str(a[x]) for x in range(2, len(a))]))


__starting_point()
