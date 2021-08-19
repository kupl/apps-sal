def RestoringRoadNetwork():
    import sys
    n = int(input())
    wf = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    # Warshall Floyd
    for i in range(n - 1):
        for j in range(i + 1, n):
            d = wf[i][j]
            # kを中継したときの距離
            for k in range(n):
                if k in (i, j):
                    continue
                num = wf[i][k] + wf[k][j]
                if num < d:
                    print((-1))
                    return
                elif num == d:
                    break
            else:
                ans += d
    else:
        print(ans)


def __starting_point():
    RestoringRoadNetwork()


__starting_point()
