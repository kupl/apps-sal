def __starting_point():
    (n, m) = input().split(' ')
    n = int(n)
    m = int(m)
    x = [int(i) for i in input().split(' ')]
    pre = [0] * (n + 2)
    tmp = 0
    for i in range(m - 1):
        (a, b) = (x[i], x[i + 1])
        if a > b:
            (a, b) = (b, a)
        if a == b:
            continue
        pre[1] += b - a
        pre[a] -= b - a
        pre[a] += b - 1
        pre[a + 1] -= b - 1
        pre[a + 1] += b - a - 1
        pre[b] -= b - a - 1
        pre[b] += a
        pre[b + 1] -= a
        pre[b + 1] += b - a
        pre[n + 1] -= b - a
    for i in range(1, n + 1):
        pre[i] += pre[i - 1]
        print(pre[i], end=' ')
    print('')


__starting_point()
