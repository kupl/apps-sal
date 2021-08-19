def main():
    (n, nc) = list(map(int, input().split()))
    d = [list(map(int, input().split())) for i in range(nc)]
    c = [list(map(int, input().split())) for i in range(n)]
    cnt = [[0 for _ in range(nc)] for eta in range(3)]
    for i in range(n):
        for j in range(n):
            eta = (i + j) % 3
            cnt[eta][c[i][j] - 1] += 1
    iwamin = 10 ** 9
    for c1 in range(nc):
        for c2 in range(nc):
            for c3 in range(nc):
                if len(set([c1, c2, c3])) < 3:
                    continue
                iwa = 0
                for c4 in range(nc):
                    iwa += cnt[0][c4] * d[c4][c1]
                    iwa += cnt[1][c4] * d[c4][c2]
                    iwa += cnt[2][c4] * d[c4][c3]
                iwamin = min(iwamin, iwa)
    print(iwamin)


def __starting_point():
    main()


__starting_point()
