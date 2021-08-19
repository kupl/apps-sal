import collections
N, A = [int(_) for _ in input().split()]
X = [int(_) for _ in input().split()]


def calc(W):
    # dp[m][s]=m枚のカードの和がsとなるような選び方の総数
    M = len(W)
    dp = [collections.defaultdict(int) for _ in range(M + 1)]
    dp[0][0] = 1
    for i, w in enumerate(W):
        for j in range(i, -1, -1):
            for k, v in list(dp[j].items()):
                dp[j + 1][k + w] += v
    return dp


dpx = calc(X)
print((sum(dpx[i][i * A] for i in range(1, N + 1))))
