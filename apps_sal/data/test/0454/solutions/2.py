(n, k) = map(int, input().split())
dp = {}
dp[0, 0, 0] = 1


def perm(i, j, k):
    if (i, j, k) in dp:
        return dp[i, j, k]
    if i == 0:
        if k == 0 and j == 0:
            return 1
        else:
            return 0
    elif k < 0 or j < 0 or i < j:
        return 0
    else:
        dp[i, j, k] = ((j + j + 1) * perm(i - 1, j, k - 2 * j) + (j + 1) * (j + 1) * perm(i - 1, j + 1, k - 2 * j) + 1 * perm(i - 1, j - 1, k - 2 * j)) % (10 ** 9 + 7)
        return dp[i, j, k]


print(perm(n, 0, k))
