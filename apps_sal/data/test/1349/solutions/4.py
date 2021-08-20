t = int(input())
INF = 548
for z in range(t):
    (n, k) = map(int, input().split())
    a = [INF] * n
    c = [int(x) for x in input().split()]
    for i in c:
        a[i - 1] = 0
    last = -INF
    for i in range(n):
        if a[i] == 0:
            last = i
        else:
            a[i] = min(a[i], i - last)
    last = INF
    for i in range(n - 1, -1, -1):
        if a[i] == 0:
            last = i
        else:
            a[i] = min(a[i], last - i)
    print(max(a) + 1)
