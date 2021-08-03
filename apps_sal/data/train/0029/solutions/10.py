t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    dct = {}
    for i in a:
        dct[i] = (-1, 0)
    now = 0
    for i in a:
        dct[i] = [now, max(dct[i][1], now - dct[i][0])]
        now += 1
    for i in dct:
        dct[i] = max(dct[i][1], (n - dct[i][0]))
    a = [(dct[i], i) for i in dct]
    a.sort()
    mini = 1000000000000000
    now = 0
    q = len(a)
    for i in range(1, n + 1):
        while now < q and a[now][0] == i:
            mini = min(mini, a[now][1])
            now += 1
        if mini == 1000000000000000:
            print(-1, end=' ')
        else:
            print(mini, end=' ')
    print()
