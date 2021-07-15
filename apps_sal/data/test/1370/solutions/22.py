#!python3

import itertools


INF = 10 ** 5

# input
H, W, K = list(map(int, input().split()))
S = [[int(e) for e in input()] for _ in range(H)]


def solve(w, l):
    n = len(l) + 1
    ans = 0
    if n == 1:
        dp = 0
        for j in range(W):
            x = w[-1][j]
            if x > K:
                return INF
            dp += x
            if dp > K:
                ans += 1
                dp = x
    else:
        dp = [0] * n
        for j in range(W):
            x = [0] * n
            b = False
            for i in range(n):
                if i == 0:
                    x[i] = w[l[i]][j]
                elif i == n - 1:
                    x[i] = w[-1][j] - w[l[-1]][j]
                else:
                    x[i] = w[l[i]][j] - w[l[i-1]][j]
                if x[i] > K:
                    return INF
                dp[i] += x[i]
                if dp[i] > K:
                    b = True
            if b:
                dp = x
                ans += 1
    return ans


def main():
    w = [S[0]]
    for i in range(1, H):
        w.append([w[i-1][j] + S[i][j] for j in range(W)])

    ans = INF
    num_list = [i for i in range(H - 1)]
    for i in range(H):
        comb_list = itertools.combinations(num_list, i)
        for l in comb_list:
            ans = min(ans, i + solve(w, l))

    print(ans)


def __starting_point():
    main()

__starting_point()
