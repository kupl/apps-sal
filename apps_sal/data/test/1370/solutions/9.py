import sys


def solve():
    input = sys.stdin.readline
    (H, W, K) = map(int, input().split())
    S = [list(map(int, list(input().strip('\n')))) for _ in range(H)]
    sumS = [[0] * (W + 1) for _ in range(H + 1)]
    for h in range(H):
        for w in range(W):
            sumS[h + 1][w + 1] = sumS[h + 1][w] + sumS[h][w + 1] - sumS[h][w] + S[h][w]
    minK = 1000000000000
    for h in range(2 ** (H - 1)):
        count = 0
        border = [0]
        k = h
        for i in range(H - 1):
            if k % 2 == 1:
                border.append(i + 1)
                count += 1
            k //= 2
        border.append(H)
        bN = len(border)
        left = 0
        ng = False
        for right in range(1, W + 1):
            for i in range(bN - 1):
                if sumS[border[i + 1]][right] - sumS[border[i + 1]][left] - sumS[border[i]][right] + sumS[border[i]][left] > K:
                    if right - 1 == left:
                        ng = True
                    else:
                        count += 1
                        left = right - 1
                    break
            if ng:
                break
        else:
            minK = min(minK, count)
    print(minK)
    return 0


def __starting_point():
    solve()


__starting_point()
