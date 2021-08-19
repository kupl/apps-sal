
def get(sp, n, k, m, d):
    hx = n // (sp * k - k + 1)
    lx = n // (sp * k)
    if(lx > m):
        return 0
    else:
        return min(m, hx) * sp


def __starting_point():
    k = input()
    lis = k.split(' ')
    # print("{}\n".format(k))
    # print("{}\n".format(lis))
    n = int(lis[0])
    k = int(lis[1])
    m = int(lis[2])
    d = int(lis[3])
    ans = -1
    for i in range(1, d + 1):
        ans = max(ans, get(i, n, k, m, d))

    print("{}\n".format(ans))


__starting_point()
