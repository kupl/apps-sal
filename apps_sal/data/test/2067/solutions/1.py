def __starting_point():
    (n, m) = map(int, input().split())
    sir = [int(input()) for i in range(n)]
    sir.append(10 ** 9)
    w = []
    b = 0
    mini = 999999
    nrSir = len(sir)
    for i in range(m):
        (x, y, z) = map(int, input().split())
        if x == 1:
            w.append(y)
    sir.sort()
    w.sort()
    nrW = len(w)
    for i in range(nrSir):
        while b < nrW and sir[i] > w[b]:
            b = b + 1
        if mini + b > nrW + i:
            mini = i - b + nrW
        if b == nrW:
            break
    print(mini)


__starting_point()
