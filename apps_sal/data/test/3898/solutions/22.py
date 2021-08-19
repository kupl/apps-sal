def run():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    i = a.index(1)
    j = b.index(1)
    ok = True
    cont = 0
    while cont < n:
        if a[i] != b[j]:
            ok = False
            break
        i = (i + 1) % n
        j = (j + 1) % n
        if a[i] == 0:
            i = (i + 1) % n
        if b[j] == 0:
            j = (j + 1) % n
        cont += 1
    print('YES' if ok else 'NO')


def __starting_point():
    run()


__starting_point()
