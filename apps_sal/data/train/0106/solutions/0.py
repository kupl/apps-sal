t = int(input())

for ti in range(t):
    n = int(input())

    lri = [None for _ in range(n)]

    for _ in range(n):
        li, ri = list(map(int, input().split()))
        lri[_] = (li, ri, _)

    lri.sort()

    t = [None for _ in range(n)]

    ct, t[lri[0][2]], eg = 1, 1, lri[0][1]

    for i in range(1, n):
        if lri[i][0] <= eg:
            t[lri[i][2]] = ct
            eg = max(eg, lri[i][1])
        else:
            ct = 3 - ct
            t[lri[i][2]] = ct
            eg = lri[i][1]

    if all(ti == 1 for ti in t):
        print(-1)
    else:
        print(*t)
