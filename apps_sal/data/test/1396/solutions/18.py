def do(l, r):
    li = 0
    ri = 0
    nl = len(l)
    nr = len(r)
    l.append(-1)
    r.append(-1)
    x = 0
    while l[li] > 0 and r[ri] > 0:
        a = 0
        c = l[li]
        while l[li] == c:
            a += 1
            li += 1
        while r[ri] == c:
            a += 1
            ri += 1
        if a < 3:
            return li + ri - a - x
        x = 1
    return li + ri - x


def s():
    [n, k, x] = list(map(int, input().split()))
    c = list(map(int, input().split()))
    res = 0
    for i in range(n):
        l = [x]
        l.extend(list(reversed(c[:i])))
        res = max(do(l, c[i:]), res)
    print(res)


s()
