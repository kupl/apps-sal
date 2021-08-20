import numpy
3
MAX = 10 ** 9 + 7


def prod_mod(la, mod):
    x = 1
    for a in la:
        x *= a
        x %= mod
    return x


def main():
    (n, k) = list(map(int, input().strip().split()))
    la = numpy.array(list(map(int, input().strip().split())))
    la.sort()
    if n == k:
        print(prod_mod(la, MAX))
    elif k % 2 == 1 and (la >= 0).sum() == 0:
        print(prod_mod(la[-k:], MAX))
    else:
        (il, ir) = (0, n - 1)
        cnt = 0
        l = []
        if k % 2 == 1:
            l.append(la[ir])
            ir -= 1
            cnt += 1
        while k - (cnt + 2) >= 0:
            if la[il] * la[il + 1] > la[ir - 1] * la[ir]:
                l.extend([la[il], la[il + 1]])
                il += 2
            else:
                l.extend([la[ir - 1], la[ir]])
                ir -= 2
            cnt += 2
        print(prod_mod(l, MAX))


def __starting_point():
    main()


__starting_point()
