def indeksTurun(a):
    for x in range(len(a) - 1):
        if a[x] > a[x + 1]:
            return x + 1
            pass
        pass
    return -1
    pass


def menaik(a, i1):
    for x in range(i1, len(a) - 1):
        if a[x] > a[x + 1]:
            return False
            pass
        pass
    return True
    pass


a = input()
a = list(map(int, input().split(" ")))

if len(a) == 1:
    print("yes")
    print("1 1")
else:
    reversed_indeks1 = -1
    for x in range(len(a) - 1):
        if a[x] > a[x + 1]:
            reversed_indeks1 = x
            break
            pass
        pass
    if reversed_indeks1 == -1:
        print("yes")
        print("1 1")
    else:
        reversed_indeks2 = len(a) - 1
        for x in range(reversed_indeks1, len(a) - 1):
            if a[x] < a[x + 1]:
                reversed_indeks2 = x
                break
        asc = True
        if reversed_indeks2 != len(a) - 1:
            asc = menaik(a, reversed_indeks2 + 1)
        if asc:
            kiri = True
            kanan = True
            if reversed_indeks1 != 0:
                if a[reversed_indeks2] < a[reversed_indeks1 - 1]:
                    kiri = False
                    pass
            if reversed_indeks2 != len(a) - 1:
                if a[reversed_indeks1] > a[reversed_indeks2 + 1]:
                    kanan = False
                    pass
                pass
                pass
            if kiri and kanan:
                print("yes")
                print("%d %d" % (reversed_indeks1 + 1, reversed_indeks2 + 1))
                pass
            else:
                print("no")
        else:
            print("no")
            pass
    pass
