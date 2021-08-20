(H, W) = list(map(int, input().split()))
G = [list(input()) for i in range(H)]
G_t = [list(x) for x in list(zip(*G))]


def Check(G, H, W):
    Paired_y = [False] * H
    for y1 in range(H):
        if Paired_y[y1]:
            continue
        for y2 in range(H):
            if y1 == y2 or Paired_y[y2]:
                continue
            Paired_x = [False] * W
            for x1 in range(W):
                if Paired_x[x1]:
                    continue
                for x2 in range(W):
                    if x1 == x2 or Paired_x[x2]:
                        continue
                    if G[y1][x1] == G[y2][x2] and G[y1][x2] == G[y2][x1]:
                        Paired_x[x1] = True
                        Paired_x[x2] = True
                        break
            if W % 2 == 1:
                if Paired_x.count(False) == 1:
                    r = Paired_x.index(False)
                    if G[y1][r] == G[y2][r]:
                        Paired_y[y1] = True
                        Paired_y[y2] = True
                        break
            elif Paired_x.count(False) == 0:
                Paired_y[y1] = True
                Paired_y[y2] = True
                break
    if H % 2 == 1:
        if Paired_y.count(False) == 1:
            return True
        else:
            return False
    elif Paired_y.count(False) == 0:
        return True
    else:
        return False


if Check(G, H, W) and Check(G_t, W, H):
    print('YES')
else:
    print('NO')
