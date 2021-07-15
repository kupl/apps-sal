t = int(input())

for w in range(t):
    n = int(input())
    a = tuple(map(int, input().split()))

    d = {}
    for i, x in enumerate(a):
        if x not in d:
            d[x] = [i + 1, i + 1]
        else:
            d[x] = [i + 1, max(d[x][1], i + 1 - d[x][0])]

    l = len(a) + 1
    for i in d:
        d[i] = max(d[i][1], l - d[i][0])

    z = {}
    for i, x in list(d.items()):
        if x in z:
            if z[x] > i:
                z[x] = i
        else:
            z[x] = i

    q = [-1 for x in range(n)]
    for i, x in list(z.items()):
        q[i - 1] = x

    q1 = []
    m = -1
    for x in q:
        if x == -1:
            q1.append(m)
        else:
            if m != -1:
                m = min(m, x)
            else:
                m = x
            q1.append(m)

    print(' '.join(str(x) for x in q1))

