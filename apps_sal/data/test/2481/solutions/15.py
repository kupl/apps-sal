def main():
    inf = float("inf")
    h, w = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(10)]
    dp1 = [[inf] * 10 for _ in range(10)]

    for i in range(10):
        for j in range(10):
            dp1[i][j] = lst[i][j]

    for k in range(1, 11):
        dp2 = [dp1[i][:] for i in range(10)]
        for i in range(10):
            for j in range(10):
                if dp2[i][j] > dp2[i][k - 1] + dp2[k - 1][j]:
                    dp1[i][j] = dp2[i][k - 1] + dp2[k - 1][j]

    wall = [list(map(int, input().split())) for _ in range(h)]
    sm = 0
    for i in range(h):
        for j in range(w):
            if wall[i][j] == -1:
                continue
            sm += dp1[wall[i][j]][1]

    print(sm)


main()
