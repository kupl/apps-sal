def Wall():
    h, w = list(map(int, input().split()))

    # Warshall Floyd配列
    wf = [list(map(int, input().split())) for _ in range(10)]

    # Warshall Floyd初期値代入
    for i in range(10):
        wf[i][i] = 0

    # Warshall Floyd
    for i in range(10):
        for j in range(10):
            for k in range(10):
                wf[j][k] = min(wf[j][i] + wf[i][k], wf[j][k])
    ans = 0
    for _ in range(h):
        a = list(map(int, input().split()))
        for v in a:
            if v == -1:
                continue
            ans += wf[v][1]
    print(ans)


def __starting_point():
    Wall()


__starting_point()
