def __starting_point():
    n, m = list(map(int, input().split()))

    A = []
    for i in range(m):
        a, b = list(map(int, input().split()))
        A.append([a, b, i, ""])

    B = sorted(A, key=lambda x: (x[0], x[1]))

    no = 1
    tmp = 0
    for b in B:
        if tmp == b[0]:
            no += 1
        else:
            tmp = b[0]
            no = 1

        cityno = str(b[0]).zfill(6) + str(no).zfill(6)
        b[3] = cityno

    C = sorted(B, key=lambda x: (x[2]))

    for c in C:
        print((c[3]))


__starting_point()
