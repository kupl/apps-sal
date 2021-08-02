# coding: utf-8


def main():
    H, W = list(map(int, input().split()))
    ans = 'Yes'
    grid = [['*'] * (W + 2) for _ in range(H + 2)]
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for i in range(H):
        S = list(input())
        for j in range(W):
            grid[i + 1][j + 1] = S[j]

    for i in range(H):
        for j in range(W):
            if grid[i + 1][j + 1] == '#':
                flg = True
                for x, y in dir:
                    if grid[i + 1 + x][j + 1 + y] == '#':
                        flg = False
                if flg:
                    ans = 'No'

    print(ans)


def __starting_point():
    main()


__starting_point()
