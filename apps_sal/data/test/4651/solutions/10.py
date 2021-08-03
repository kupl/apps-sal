q = int(input())
for __ in [0] * q:
    n = int(input())
    a = list(map(int, input().split()))
    idx = [-1] * (n + 1)
    for i, e in enumerate(a):
        idx[e] = i

    res = []
    k = -1
    for i, e in enumerate(idx):
        if e == -1:
            continue
        if e > k:
            res.append(i)
            if i != 1:
                if res[-1] < res[-2]:
                    res[-1], res[-2] = res[-2], res[-1]
            for i in range(k + 1, e):
                res.append(a[i])
            k = e
    for e in res:
        if e != res[-1]:
            print(e, end=' ')
        else:
            print(e)
