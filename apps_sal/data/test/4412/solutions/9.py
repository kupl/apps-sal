q = int(input())
for query in range(q):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    l.reverse()
    wy = -1000000000000
    a = [l[0]]
    u = 1
    while u < n:
        if l[u] != l[u - 1]:
            a.append(l[u])
        if len(a) > 4:
            break
        u += 1
    if len(a) > 3 and a[1] == a[0] / 2 and (a[2] == a[0] / 3) and (a[3] == a[0] / 5) or (len(a) > 4 and a[1] == a[0] / 2 and (a[2] == a[0] / 3) and (a[3] == a[0] / 4) and (a[4] == a[0] / 5)):
        wy = a[1] + a[2] + a[3]
    nowa = [l[i] for i in range(n) if l[0] % l[i] != 0]
    nowa.sort()
    nowa.reverse()
    if len(nowa) > 0:
        part = 0
        for i in range(1, len(nowa)):
            if nowa[0] % nowa[i] != 0:
                part = nowa[i]
                break
        wyn = l[0] + nowa[0] + part
    else:
        wyn = l[0]
    print(max(wyn, wy))
