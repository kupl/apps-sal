(n, m) = [int(x) for x in input().split()]


def su(p):
    c = 0
    for i in range(p + 1):
        c += i
    return c


l = m - n
print(su(l - 1) - n)
