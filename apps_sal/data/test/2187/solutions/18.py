for _ in range(int(input())):
    n = int(input())
    a = [0] + [*list(map(int, input().split()))]
    d = [0] * (n + 1)
    for i in range(1, n + 1):
        d[i] = a[i] - a[i - 1]
    s = 0
    i = 1
    while i <= n:
        if d[i] >= 0:
            i += 1
            continue
        mn = d[i]
        while i + 1 <= n and d[i + 1] < 0:
            i += 1
            mn += d[i]
        s += -1 * mn
        i += 1
    print(s)
