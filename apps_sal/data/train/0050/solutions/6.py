q = int(input())
for rwier in range(q):
    n = int(input())
    l = list(map(int, input().split()))
    j = l.count(1)
    d = l.count(2)
    pr = [0] * n
    le = [0] * n
    pr[0] = 1 if l[n] == 1 else -1
    le[0] = 1 if l[n - 1] == 1 else -1
    for i in range(1, n):
        pr[i] = pr[i - 1] + (1 if l[n + i] == 1 else -1)
        le[i] = le[i - 1] + (1 if l[n - i - 1] == 1 else -1)
    if j - d < 0:
        for i in range(n):
            pr[i] = -pr[i]
            le[i] = -le[i]
    ab = abs(j - d)
    if ab == 0:
        print(0)
    else:
        najwp = [123456789] * (2 * n + 1)
        najwl = [123456789] * (2 * n + 1)
        le = [0] + le
        pr = [0] + pr
        for i in range(n + 1):
            if pr[i] >= 0 and najwp[pr[i]] == 123456789:
                najwp[pr[i]] = i
            if le[i] >= 0 and najwl[le[i]] == 123456789:
                najwl[le[i]] = i
        wyn = 41343443143
        for i in range(ab + 1):
            if najwp[i] + najwl[ab - i] < wyn:
                wyn = najwp[i] + najwl[ab - i]
        print(wyn)
