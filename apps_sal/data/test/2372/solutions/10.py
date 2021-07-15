from collections import deque


def solve():
    H, W = list(map(int, input().split()))
    CH, CW = list(map(int, input().split()))
    DH, DW = list(map(int, input().split()))
    S = ["##"+input()+"##" for _ in range(H)]
    for i in range(2):
        S.insert(0, "#"*(W+4))
        S.append("#"*(W+4))

    inf = int(1e9)
    cost = [[inf for _ in range(W+4)] for _ in range(H+4)]
    cost0 = deque()
    ans = -1

    cost0.append((CH+1, CW+1, 0))
    cost[CH+1][CW+1] = 0

    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    warp = [(i, j) for i in range(-2, 3) for j in range(-2, 3) if (i, j) not in [(0, 0)]+move]

    cost1 = deque()

    while cost0:
        h, w, c = cost0.popleft()
        cost1.append((h, w, c))

        for i, j in move:
            dh = h+i
            dw = w+j
            if S[dh][dw] == "." and c < cost[dh][dw]:
                cost[dh][dw] = c
                cost0.appendleft((dh, dw, cost[dh][dw]))

        if len(cost0) == 0:
            while cost1:
                h, w, c = cost1.popleft()
                for i, j in warp:
                    dh = h+i
                    dw = w+j
                    if S[dh][dw] == "." and c+1 < cost[dh][dw]:
                        cost[dh][dw] = c+1
                        cost0.append((dh, dw, cost[dh][dw]))

        if cost[DH+1][DW+1] != inf:
            ans = cost[DH+1][DW+1]

    print(ans)


def __starting_point():
    solve()

__starting_point()
