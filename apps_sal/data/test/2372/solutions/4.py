import sys
input = sys.stdin.readline


def solve():
    dxys = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    H, W = list(map(int, input().split()))
    Ch, Cw = list(map(int, input().split()))
    Dh, Dw = list(map(int, input().split()))
    Sss = ['#' * (W + 4)] + ['#' * (W + 4)] + ['##' + input().rstrip() + '##' for _ in range(H)] + ['#' * (W + 4)] + ['#' * (W + 4)]

    Ch, Cw, Dh, Dw = Ch + 1, Cw + 1, Dh + 1, Dw + 1

    usedss = [[0] * (W + 4) for _ in range(H + 4)]
    for x in range(H + 4):
        for y in range(W + 4):
            if Sss[x][y] == '#':
                usedss[x][y] = 1

    ans = 0
    vs = set([(Ch, Cw)])
    vNews = set([(Ch, Cw)])
    usedss[Ch][Cw] = 1
    while True:
        while vs:
            v2s = set()
            for x, y in vs:
                for dx, dy in dxys:
                    x2, y2 = x + dx, y + dy
                    if usedss[x2][y2]:
                        continue
                    v2s.add((x2, y2))
                    vNews.add((x2, y2))
                    usedss[x2][y2] = 1
            vs = v2s

        if usedss[Dh][Dw]:
            print(ans)
            break

        if not vNews:
            print((-1))
            break

        vs = set()
        for x, y in vNews:
            for dx in range(-2, 3):
                for dy in range(-2, 3):
                    x2, y2 = x + dx, y + dy
                    if usedss[x2][y2]:
                        continue
                    vs.add((x2, y2))
                    usedss[x2][y2] = 1

        ans += 1
        vNews = set(vs)


solve()
