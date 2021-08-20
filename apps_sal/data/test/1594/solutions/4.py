def f():
    (n, m) = map(int, input().split())
    d = [0] * (n + 1)
    for i in range(1, n + 1):
        (a, b) = map(int, input().split())
        d[i] = d[i - 1] + a * b
    t = list(map(int, input().split()))
    j = 0
    for i in range(1, n + 1):
        while t[j] <= d[i]:
            t[j] = i
            j += 1
            if j == m:
                print('\n'.join((str(k) for k in t)))
                return


f()
