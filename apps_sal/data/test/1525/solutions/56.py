from itertools import product


def patterns(w):
    res = []
    for pt in product([0, 1], repeat=w):
        valid = True
        for i in range(w - 1):
            if pt[i] == pt[i + 1] == 1:
                valid = False
                break
        if valid:
            res.append(pt)
    return res


def submit():
    (h, w, k) = [int(e) for e in input().split()]
    dp = [[0 for _ in range(w)] for _ in range(h + 1)]
    dp[0][0] = 1
    modp = 10 ** 9 + 7
    pts = patterns(w - 1)
    for i in range(1, h + 1):
        for j in range(w):
            for pt in pts:
                if j > 0 and pt[j - 1] == 1:
                    dp[i][j - 1] += dp[i - 1][j]
                    dp[i][j - 1] %= modp
                elif j < w - 1 and pt[j] == 1:
                    dp[i][j + 1] += dp[i - 1][j]
                    dp[i][j + 1] %= modp
                else:
                    dp[i][j] += dp[i - 1][j]
                    dp[i][j] %= modp
    print(dp[h][k - 1])


submit()
