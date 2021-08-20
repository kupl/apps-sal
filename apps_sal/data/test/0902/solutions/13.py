def read():
    return tuple(map(int, input().split()))


def main():
    (n, k) = read()
    l = list(read())
    ps = {}

    def add(p):
        if not p in ps:
            ps[p] = 1
        else:
            ps[p] += 1
        return (ps[p] >= k, p)
    newl = []
    while len(l) > 1:
        (v1, v2) = (l[0], l[1])
        if v1 > v2:
            l.pop(1)
            newl += [v2]
            addk = add(v1)
        else:
            l.pop(0)
            newl += [v1]
            addk = add(v2)
        if addk[0]:
            return addk[1]
    return l[0]


print(main())
