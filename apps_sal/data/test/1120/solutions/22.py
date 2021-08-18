n = int(input())


def naive(n):
    c = 0
    while n != 0:
        c += 1
        n -= max([int(x) for x in list(str(n))])
    print(c)


naive(n)
