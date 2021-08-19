import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline


def in_n():
    return int(readline())


def in_nn():
    return list(map(int, readline().split()))


def in_nl():
    return list(map(int, readline().split()))


def in_na():
    return list(map(int, read().split()))


def in_s():
    return readline().rstrip().decode('utf-8')


def main():
    (H, W, D) = in_nn()
    A = [list(map(int, readline().split())) for _ in range(H)]
    Q = in_n()
    LR = [list(map(int, readline().split())) for _ in range(Q)]
    grid = [tuple()] * (H * W + 1)
    for y in range(H):
        for x in range(W):
            num = A[y][x]
            grid[num] = (x + 1, y + 1)
    move = [[] for _ in range(D)]
    for i in range(D):
        if i == 0:
            s = D
        else:
            s = i
        while s <= H * W:
            move[i].append(grid[s])
            s += D
    d = [[] for _ in range(D)]
    for i in range(D):
        d[i].append(0)
        for j in range(len(move[i]) - 1):
            (x, y) = move[i][j]
            (nx, ny) = move[i][j + 1]
            d[i].append(abs(nx - x) + abs(ny - y))
    for i in range(D):
        for j in range(len(d[i]) - 1):
            d[i][j + 1] += d[i][j]
    ans = [0] * Q
    for i in range(Q):
        (l, r) = LR[i]
        (q1, rr) = divmod(l, D)
        (q2, _) = divmod(r, D)
        if rr == 0:
            ans[i] = d[rr][q2 - 1] - d[rr][q1 - 1]
        else:
            ans[i] = d[rr][q2] - d[rr][q1]
    print('\n'.join(map(str, ans)))


def __starting_point():
    main()


__starting_point()
