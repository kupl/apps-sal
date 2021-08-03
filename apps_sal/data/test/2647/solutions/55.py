import sys
from collections import Counter
from collections import deque

input = sys.stdin.readline


def main():
    H, W = list(map(int, input().split()))
    grid = []
    wh = 0
    for _ in range(H):
        tmp = list(input()[:-1])
        wh += Counter(tmp)['.']
        grid.append(tmp)
    check = [[0] * W for _ in range(H)]

    # digtmp
    digtmp = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    #digtmp = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]

    # BFS
    # please prefer objects:
    #  H: height.
    #  W: width
    #  field: maze field made of '.', '#'.
    #  check: check field
    que = deque([(0, 0)])
    check[0][0] = 1
    while True:
        a, b = que.popleft()
        for dx, dy in digtmp:
            x = a + dx
            y = b + dy
            if not (0 <= x < H and 0 <= y < W):
                continue
            if check[x][y] != 0 or grid[x][y] == '#':
                continue
            check[x][y] = check[a][b] + 1
            que.append((x, y))
        if len(que) == 0:
            break

    if check[H - 1][W - 1] == 0:
        print((-1))
    else:
        print((wh - check[H - 1][W - 1]))


def __starting_point():
    main()


__starting_point()
