t = int(input())


def prov1(a):
    pp = a[0] * a[-1]
    for i in range(len(a)):
        if a[i] * a[-1 - i] != pp: return -1
    return pp


def kkk(a):
    i = 2
    d = 0
    while i * i < a:
        if a % i == 0:
            d += 2
        i += 1
    if i * i == a: d += 1
    return d


def koka(a, b):
    ans = 0
    while a % b == 0:
        a = a // b
        ans += 1
    return ans


for i in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    y = prov1(a)
    if y == -1:
        print(-1)
    else:
        yy = kkk(a[0])
        if yy > 0: print(-1)
        else:
            u = kkk(a[-1]) + 2
            z = koka(a[-1], a[0])
            if z == 0: d = u * 2 - 2
            else:
                d = (u // (z + 1)) * (z + 2) - 2
            if d == n:
                print(y)
            else:
                print(-1)
