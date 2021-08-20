import sys


def sr():
    return sys.stdin.readline().rstrip()


def ir():
    return int(sr())


def lr():
    return list(map(int, sr().split()))


def resolve():
    (H, W, K) = lr()
    S = []
    for i in range(H):
        S.append([int(s) for s in sr()])
    ans = 2000
    idx = [0] * H
    for div in range(1 << H - 1):
        g = 0
        for i in range(H):
            idx[i] = g
            if div >> i & 1:
                g += 1
        g += 1
        c = [[0] * W for i in range(g)]
        for i in range(H):
            for j in range(W):
                c[idx[i]][j] += S[i][j]
        ok = True
        for i in range(g):
            for j in range(W):
                if c[i][j] > K:
                    ok = False
        if not ok:
            continue
        num = g - 1
        now = [0] * g

        def add(j):
            for i in range(g):
                now[i] += c[i][j]
            for i in range(g):
                if now[i] > K:
                    return False
            return True
        for j in range(W):
            if not add(j):
                num += 1
                now = [0] * g
                add(j)
        ans = min(ans, num)
    print(ans)


resolve()
