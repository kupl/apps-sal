import sys
input = sys.stdin.readline


def main():
    H, W = map(int, input().split())
    R = list(map(int, input().split()))
    C = list(map(int, input().split()))

    grid1 = [[-1] * W for _ in range(H)]
    grid2 = [[-1] * W for _ in range(H)]

    for i, r in enumerate(R):
        for j in range(r):
            grid1[i][j] = 1
        if r <= W - 1:
            grid1[i][r] = 0

    for i, c in enumerate(C):
        for j in range(c):
            grid2[j][i] = 1
        if c <= H - 1:
            grid2[c][i] = 0

    ok = True
    prob = 0
    for h in range(H):
        for w in range(W):
            if grid1[h][w] == -1 and grid2[h][w] == -1:
                prob += 1
            elif grid1[h][w] == -1 or grid2[h][w] == -1:
                continue
            elif grid1[h][w] != grid2[h][w]:
                ok = False

    if not ok:
        print(0)
    else:
        mod = int(1E9 + 7)
        ans = 1
        for _ in range(prob):
            ans = ans * 2 % mod
        print(ans)


def __starting_point():
    main()


__starting_point()
