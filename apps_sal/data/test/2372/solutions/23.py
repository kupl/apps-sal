from collections import deque


def solve():
    h, w = list(map(int, input().split()))
    ch, cw = list(map(int, input().split()))
    Dh, Dw = list(map(int, input().split()))

    M = ['##' + input() + '##' for _ in range(h)]
    for i in range(2):
        M.insert(0, '#' * (w + 4))
        M.append('#' * (w + 4))

    INF = float('inf')
    cost = [[INF for _ in range(w + 4)] for _ in range(h + 4)]
    cost0 = deque()
    ans = -1

    cost0.append((ch + 1, cw + 1, 0))
    cost[ch + 1][cw + 1] = 0

    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    warp = [(i, j) for i in range(-2, 3) for j in range(-2, 3) if (i, j) not in [(0, 0)] + move]

    cost1 = deque()

    while cost0:
        h, w, c = cost0.popleft()
        cost1.append((h, w, c))

        for i, j in move:
            dh = h + i
            dw = w + j
            if M[dh][dw] == '.' and c < cost[dh][dw]:  # コストが高いところから低いところに戻らないようにするため
                cost[dh][dw] = c
                cost0.appendleft((dh, dw, cost[dh][dw]))

        if len(cost0) == 0:
            while cost1:
                h, w, c = cost1.popleft()
                for i, j in warp:
                    dh = h + i
                    dw = w + j
                    if M[dh][dw] == '.' and c + 1 < cost[dh][dw]:  # 無駄なワープをなくすため
                        cost[dh][dw] = c + 1
                        cost0.append((dh, dw, cost[dh][dw]))
        if cost[Dh + 1][Dw + 1] != INF:
            ans = cost[Dh + 1][Dw + 1]

    print(ans)


def __starting_point():
    solve()


__starting_point()
