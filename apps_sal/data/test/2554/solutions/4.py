
tt = int(input())

for loop in range(tt):

    n = int(input())
    a = list(map(int, input().split()))

    e = [0]
    o = [0]

    for i in range(n):
        if i % 2 == 0:
            e.append(e[-1] + a[i])
            o.append(o[-1])
        else:
            e.append(e[-1])
            o.append(o[-1] + a[i])

    eo = []
    for i in range(n + 1):
        eo.append(o[i] - e[i])

    nmin = float("inf")
    ans = 0
    for i in range(0, n + 1, 2):
        ans = max(ans, eo[i] - nmin)
        nmin = min(nmin, eo[i])

    nmin = float("inf")
    for i in range(1, n + 1, 2):
        ans = max(ans, eo[i] - nmin)
        nmin = min(nmin, eo[i])

    ori = 0
    for i in range(0, n, 2):
        ori += a[i]

    print(ori + ans)
