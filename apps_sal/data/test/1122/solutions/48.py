def resolve():
    (N, M) = map(int, input().split())
    if M == 1:
        print(1, 2)
        return
    i1 = 1
    i2 = M + 2
    for diff in range(M, 0, -1):
        print(i1, i1 + diff)
        i1 += 1
        (i1, i2) = (i2, i1)


def __starting_point():
    resolve()


__starting_point()
