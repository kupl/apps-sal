def I():
    return int(input())


def IL():
    return list(map(int, input().split()))


def IM():
    return map(int, input().split())


def IS():
    return input()


def ISL():
    return list(input())


(n, h) = IM()
l = IL()


def can_put(mi):
    if mi == 0:
        return l[0] <= h
    z = sorted(l[0:mi + 1])
    req = 0
    if mi % 2 == 0:
        req += z[0]
        for i in range(1, mi + 1, 2):
            req += max(z[i], z[i + 1])
    else:
        for i in range(0, mi + 1, 2):
            req += max(z[i], z[i + 1])
    return req <= h


lo = 0
hi = n - 1
ans = 0
while lo <= hi:
    mi = lo + hi >> 1
    if can_put(mi):
        ans = mi
        lo = mi + 1
    else:
        hi = mi - 1
print(ans + 1)
