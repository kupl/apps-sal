def divider(a):
    t = sum(a)
    d = []
    d.append(-t)
    for i in range(len(a)):
        t -= 2 * a[i]
        d.append(-t)
        if t == 0:
            return ("YES")
    for i in range(len(a)):
        s = 2 * a[i]
        j = binary(d, s)
        if j > i and j != -1:
            return ("YES")
        j = binary(d, -s)
        if i >= j and j != -1:
            return ("YES")
    return ("NO")


def binary(a, value):
    hi = len(a)
    lo = -1
    while (lo + 1 < hi):
        mi = (lo + hi) // 2
        if a[mi] == value:
            return mi
        if a[mi] < value:
            lo = mi
        else:
            hi = mi
    return -1


def __starting_point():
    n = input()
    a = [int(i) for i in input().split()]
    print(divider(a))

__starting_point()
