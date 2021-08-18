from collections import deque


def main():
    from sys import stdin
    readline = stdin.readline

    from builtins import max, min, range

    INF = 10 ** 6

    H, W = list(map(int, readline().split()))
    C1, C2 = [int(x) - 1 for x in readline().split()]
    D1, D2 = [int(x) - 1 for x in readline().split()]
    S = [readline()[:-1] for _ in range(H)]

    t = [[INF] * W for _ in range(H)]

    for h in range(H):
        Sh = S[h]
        th = t[h]
        for w in range(W):
            if Sh[w] == '
            th[w] = -1

    q = deque([(C1, C2)])
    a = 0
    t[C1][C2] = a

    while q:
        warpq = []
        while q:
            h, w = q.popleft()
            warpq.append((h, w))
            if 0 < h and t[h - 1][w] > a:
                t[h - 1][w] = a
                q.append((h - 1, w))
            if H - 1 > h and t[h + 1][w] > a:
                t[h + 1][w] = a
                q.append((h + 1, w))
            if 0 < w and t[h][w - 1] > a:
                t[h][w - 1] = a
                q.append((h, w - 1))
            if w < W - 1 and t[h][w + 1] > a:
                t[h][w + 1] = a
                q.append((h, w + 1))

        if t[D1][D2] != INF:
            break

        a += 1

        for h, w in warpq:
            for i in range(max(0, h - 2), min(H, h + 3)):
                ti = t[i]
                for j in range(max(0, w - 2), min(W, w + 3)):
                    if ti[j] > a:
                        ti[j] = a
                        q.append((i, j))

    if t[D1][D2] == INF:
        print((-1))
    else:
        print((t[D1][D2]))


main()
