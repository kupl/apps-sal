def main():
    na = list(map(int, input().split()))
    N = na[0]
    K = na[1]
    x = []
    y = []
    c = []
    for i in range(N):
        sa = input().split()
        x.append(int(sa[0]))
        y.append(int(sa[1]))
        c.append(True if sa[2] == 'W' else False)
    hopes = [[0 for j in range(K)] for i in range(K)]
    ysum = [[0 for j in range(K * 2)] for i in range(K)]
    score = 0
    for i in range(N):
        xmod = x[i] % K
        ymod = y[i] % K
        f = (int(x[i] / K) + int(y[i] / K)) % 2 == 1
        c[i] ^= f
        if c[i]:
            score += 1
        h = -1 if c[i] else 1
        hopes[xmod][ymod] += h
    for i in range(K):
        s = 0
        for j in range(K):
            s += hopes[i][j]
            ysum[i][j] = s
        for j in range(K):
            s -= hopes[i][j]
            ysum[i][K + j] = s
    smax = 0
    for j in range(K):
        s = 0
        for i in range(K):
            s += ysum[i][K + j]
        for i in range(K):
            s += ysum[i][j] - ysum[i][K + j]
            smax = max(smax, s)
        for i in range(K):
            s -= ysum[i][j] - ysum[i][K + j]
            smax = max(smax, s)
    print(score + smax)


def __starting_point():
    main()


__starting_point()
