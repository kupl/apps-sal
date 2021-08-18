mod = 998244353
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = dict()
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    l = list()
    for i in d:
        l.append((d[i], i))
    l.sort(reverse=True)
    c = 0
    lim = l[0][0]
    extra = 0
    r = 0
    for i in l:
        if i[0] == lim:
            r += 1
        else:
            extra += i[0]
    if lim == 1:
        print(n)
    else:
        r += extra // (lim - 1)
        print(r - 1)
