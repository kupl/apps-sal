def sv(N, M, K, X, Y):
    X -= 1
    Y -= 1
    if N > 1:
        rounds = K // ((N - 1) * M)
        rem = K % ((N - 1) * M)
        gd = [[0] * M for n in range(N)]
        for m in range(0, M):
            gd[0][m] = (rounds + 1) // 2
            gd[N - 1][m] = rounds // 2
        for n in range(1, N - 1):
            for m in range(0, M):
                gd[n][m] = rounds
        if rounds % 2 == 1:
            for n in range(N - 1, -1, -1):
                if not rem: break
                for m in range(0, M):
                    if not rem: break
                    rem -= 1
                    gd[n][m] += 1
        else:
            for n in range(0, N):
                if not rem: break
                for m in range(0, M):
                    if not rem: break
                    rem -= 1
                    gd[n][m] += 1
    else:
        rounds = K // M
        rem = K % M
        gd = [[rounds] * M]
        for m in range(rem):
            gd[0][m] += 1
    a1 = max(max(x) for x in gd)
    a2 = min(min(x) for x in gd)
    a3 = gd[X][Y]
    print(a1, a2, a3)


N, M, K, X, Y = list(map(int, input().split()))
sv(N, M, K, X, Y)
