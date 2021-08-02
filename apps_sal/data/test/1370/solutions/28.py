from itertools import groupby, accumulate, product, permutations, combinations


def solve():
    H, W, K = list(map(int, input().split()))
    S = [input() for _ in range(H)]
    cum = [[0] * (W + 1) for _ in range(H + 1)]
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            cum[i][j] = cum[i - 1][j] + cum[i][j - 1] - cum[i - 1][j - 1] + int(S[i - 1][j - 1])
    ans = 2000
    for p in product([0, 1], repeat=H - 1):
        line = [0]
        p = list(p)
        cnt = sum(p)
        for i in range(1, H):
            if p[i - 1] == 1:
                line.append(i)
        line.append(H)
        w_s = 0
        w_e = 1
        b = False
        while w_e <= W:
            for i in range(len(line) - 1):
                h_s = line[i]
                h_e = line[i + 1]
                white = cum[h_e][w_e] + cum[h_s][w_s] - cum[h_e][w_s] - cum[h_s][w_e]
                if white > K:
                    if w_e == w_s + 1:
                        b = True
                        break
                    else:
                        w_s = w_e - 1
                        cnt += 1
                        break
            if b == True:
                break
            w_e += 1
        else:
            ans = min(ans, cnt)
    return ans


print((solve()))
