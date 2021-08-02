def solve():
    H, W = map(int, input().split())

    G = [[1 if s == '*' else 0 for s in input()] for _ in range(H)]

    h = -1
    cnt = 0
    for i, g in enumerate(G):
        cnt += sum(g)
        if sum(g) > 1:
            if h == -1:
                h = i
            else:
                return False

    G = list(map(list, zip(*G)))
    w = -1
    for i, g in enumerate(G):
        if sum(g) > 1:
            if w == -1:
                w = i
            else:
                return False

    G = list(map(list, zip(*G)))

    c, c1, c2, c3, c4 = 1, 0, 0, 0, 0
    for i in range(w + 1, W):
        if not G[h][i]:
            break
        c1 += 1
    for i in range(w - 1, -1, -1):
        if not G[h][i]:
            break
        c2 += 1
    for i in range(h + 1, H):
        if not G[i][w]:
            break
        c3 += 1
    for i in range(h - 1, -1, -1):
        if not G[i][w]:
            break
        c4 += 1
    c += c1 + c2 + c3 + c4
    if c == cnt and c1 * c2 * c3 * c4:
        return True
    return False


if solve():
    print('YES')
else:
    print('NO')
