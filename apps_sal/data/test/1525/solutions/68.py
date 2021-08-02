from itertools import combinations

H, W, K = map(int, input().split())
dp = [[0 for i in range(W)] for j in range(H + 1)]

mod = 10**9 + 7

if W == 1:
    if K == 1:
        print(1)
    else:
        print(0)
    return

memo = {}


def is_separate(c):
    for i in range(len(c) - 1):
        if c[i + 1] - c[i] == 1:
            return False
    return True


def n_select(occupied):
    if memo.get(occupied):
        return memo[occupied]
    else:
        count = 1
        if len(occupied) == 1:
            for r in range(1, W // 2 + 1):
                for c in combinations(range(W - 1), r=r):
                    if occupied[0] - 1 not in c and occupied[0] not in c:
                        if is_separate(c):
                            count += 1
        if len(occupied) == 2:
            for r in range(1, W // 2 + 1):
                for c in combinations(range(W - 1), r=r):
                    if occupied[0] - 1 not in c and occupied[0] not in c and occupied[0] + 1 not in c:
                        if is_separate(c):
                            count += 1
    memo[occupied] = count
    return count


dp[0][0] = 1
for i in range(1, H + 1):
    for j in range(W):
        if j == 0:
            dp[i][j] = dp[i - 1][j] * n_select((j,)) + dp[i - 1][j + 1] * n_select((j, j + 1))
        elif j == W - 1:
            dp[i][j] = dp[i - 1][j] * n_select((j,)) + dp[i - 1][j - 1] * n_select((j - 1, j))
        else:
            dp[i][j] = dp[i - 1][j] * n_select((j,)) + dp[i - 1][j + 1] * n_select((j, j + 1)) + dp[i - 1][j - 1] * n_select((j - 1, j))

print(dp[-1][K - 1] % mod)
