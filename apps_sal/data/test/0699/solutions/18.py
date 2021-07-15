def __starting_point():
    y, k, n = str(input()).split()
    y = int(y)
    k = int(k)
    n = int(n)
    res = list()
    head = y // k
    tail = n // k
    for i in range(head, tail + 1):
        v = i * k
        if y < v <= n:
            res.append(str(v - y))
    if len(res) > 0:
        print(' '.join(res))
    else:
        print(-1)

__starting_point()
