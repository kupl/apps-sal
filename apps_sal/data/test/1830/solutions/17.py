def pro():
    (n, m) = map(int, input().split())
    x = [False for i in range(n)]
    x1 = n
    y = [False for i in range(n)]
    y1 = n
    for i in range(m):
        (k, l) = map(int, input().split())
        if not x[k - 1]:
            x[k - 1] = True
            x1 -= 1
        if not y[l - 1]:
            y[l - 1] = True
            y1 -= 1
        print(x1 * y1, end=' ')


pro()
