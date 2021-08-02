def primenum(N, a):
    """i<Nのiについて，iより小さい素数の数をaにリストにする"""
    b = [1] * N
    d = [0] * N
    b[0] = 0
    b[1] = 0
    i = 2
    while i * i < N:
        k = 2
        while i * k < N:
            b[i * k] = 0
            k += 1
        for j in range(i + 1, N):
            if b[j] == 1:
                break
        i = j
    c = [0]
    for i in range(3, N):
        if b[i] == 1 and b[(i + 1) // 2] == 1:
            d[i] = 1

    for i in range(1, N):
        c.append(c[i - 1] + d[i - 1])
    return c


Q = int(input())
l = [0] * Q
r = [0] * Q
for i in range(0, Q):
    l[i], r[i] = map(int, input().split())
c = []
c = primenum(110000, c)
for g in range(0, Q):
    print(c[r[g] + 1] - c[l[g]])
