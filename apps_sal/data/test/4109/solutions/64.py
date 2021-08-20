def __starting_point():
    (n, m, a) = list(map(int, input().split()))
    A = []
    for i in range(n):
        cmd = list(map(int, input().split()))
        A.append(cmd)
    INF = 10 ** 19
    ans = INF
    for x in range(2 ** n):
        ALG = [0] * m
        gokei = 0
        for y in range(n):
            if x >> y & 1:
                for j in range(m):
                    ALG[j] += A[y][j + 1]
                gokei += A[y][0]
        algflg = True
        for k in ALG:
            if k < a:
                algflg = False
                break
        if algflg:
            ans = min(ans, gokei)
    if ans == INF:
        print('-1')
    else:
        print(ans)


__starting_point()
