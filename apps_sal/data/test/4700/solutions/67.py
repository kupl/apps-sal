def __starting_point():

    # 隣接リスト(graph)
    n, m = list(map(int, input().split()))
    H = [int(h) for h in input().split()]

    graph = [[]for _ in range(n)]

    for _ in range(m):
        a, b = list(map(int, input().split()))
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    # このリストから相手との関係を調べてよい展望台かどうか調べる？
    good = 0
    for i, g in enumerate(graph):
        moto = H[i]
        flg = True
        for sk in g:
            saki = H[sk]
            if moto <= saki:
                flg = False
                break
        if flg:
            good += 1
    print(good)


__starting_point()
