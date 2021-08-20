import sys


def solve():
    input = sys.stdin.readline
    (H, W, K) = map(int, input().split())
    S = [input().strip('\n') for _ in range(H)]
    Ans = 10 ** 20
    Wcount = [[0 for _ in range(W + 1)] for _ in range(H + 1)]
    for h in range(H):
        for w in range(W):
            Wcount[h + 1][w + 1] = Wcount[h][w + 1] + Wcount[h + 1][w] - Wcount[h][w] + int(S[h][w])
    Ans = H * W + 1
    for i in range(2 ** (H - 1)):
        B = [0]
        d = i
        Hcount = 0
        for j in range(H - 1):
            if d % 2 == 1:
                B.append(j + 1)
                Hcount += 1
            d //= 2
        B.append(H)
        leftbound = 0
        TotalBound = Hcount
        NG = False
        for w in range(1, W + 1):
            for b in range(Hcount + 1):
                if Wcount[B[b + 1]][w] - Wcount[B[b + 1]][leftbound] - Wcount[B[b]][w] + Wcount[B[b]][leftbound] > K:
                    if leftbound + 1 == w:
                        NG = True
                    else:
                        TotalBound += 1
                        leftbound = w - 1
                    break
            if NG:
                break
        else:
            Ans = min(TotalBound, Ans)
    print(Ans)
    return 0


def __starting_point():
    solve()


__starting_point()
