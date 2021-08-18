
def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    WL = list(range(W))
    WLR = WL[::-1]

    path = []
    for h in range(H):
        if h % 2 == 0:
            for w in WL:
                path.append((h, w))
        else:
            for w in WLR:
                path.append((h, w))
    ret = []
    for i in range(H * W - 1):
        h, w = path[i]
        if A[h][w] % 2 == 1:
            ret.append(i)
            hn, wn = path[i + 1]
            A[hn][wn] += 1

    print(len(ret))
    for i in ret:
        h, w = path[i]
        nh, nw = path[i + 1]
        print(h + 1, w + 1, nh + 1, nw + 1)


def __starting_point():
    main()


__starting_point()
