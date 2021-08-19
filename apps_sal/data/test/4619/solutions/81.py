import sys
input = sys.stdin.readline


def read():
    (W, H, N) = list(map(int, input().strip().split()))
    XYA = []
    for i in range(N):
        (x, y, a) = list(map(int, input().strip().split()))
        XYA.append((x, y, a))
    return (W, H, N, XYA)


def solve(W, H, N, XYA):
    S = [[0 for j in range(W + 1)] for i in range(H + 1)]
    for (x, y, a) in XYA:
        if a == 1:
            (lt, rt, lb, rb) = ((0, 0), (x, 0), (0, H), (x, H))
        elif a == 2:
            (lt, rt, lb, rb) = ((x, 0), (W, 0), (x, H), (W, H))
        elif a == 3:
            (lt, rt, lb, rb) = ((0, 0), (W, 0), (0, y), (W, y))
        elif a == 4:
            (lt, rt, lb, rb) = ((0, y), (W, y), (0, H), (W, H))
        S[lt[1]][lt[0]] += 1
        S[rt[1]][rt[0]] -= 1
        S[lb[1]][lb[0]] -= 1
        S[rb[1]][rb[0]] += 1
    for i in range(H):
        for j in range(W + 1):
            S[i + 1][j] += S[i][j]
    for i in range(H + 1):
        for j in range(W):
            S[i][j + 1] += S[i][j]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == 0:
                ans += 1
    return ans


def __starting_point():
    inputs = read()
    print(solve(*inputs))


__starting_point()
