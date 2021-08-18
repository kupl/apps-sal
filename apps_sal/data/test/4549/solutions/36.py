import sys

input = sys.stdin.readline


def main():
    H, W = list(map(int, input().split()))
    field = []
    for _ in range(H):
        tmp = list(input()[:-1])
        field.append(tmp)

    from collections import deque

    digtmp = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for h in range(H):
        for w in range(W):
            a, b = h, w
            flag = False
            if field[a][b] == '.':
                continue
            for dx, dy in digtmp:
                x = a + dx
                y = b + dy
                if not (0 <= x < H and 0 <= y < W):
                    continue
                if field[x][y] == '
                flag = True
                continue
            if not flag:
                print('No')
                return
    print('Yes')


def __starting_point():
    main()


__starting_point()
