

def main():
    H, W, K = list(map(int, input().split()))

    if W == 1:
        return 1

    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1

    bridges_list = []

    def preset(i, bridges, n_cand):
        if i == n_cand:
            bridges_list.append(bridges)
            return None

        if i - 1 in bridges:
            preset(i + 1, bridges, n_cand)
        else:
            bridges_1 = bridges[:]
            bridges_2 = bridges[:]
            bridges_1.append(i)

            preset(i + 1, bridges_1, n_cand)
            preset(i + 1, bridges_2, n_cand)

    preset(0, [], W - 1)

    n_bridges = [0] * (W - 1)
    for bridges in bridges_list:
        for x in bridges:
            n_bridges[x] += 1

    n_all_cands = len(bridges_list)

    dp[0][0] = (n_all_cands - n_bridges[0])
    dp[0][1] = n_bridges[0]

    for i in range(H - 1):
        for j in range(W):
            if j == 0:
                dp[i + 1][j] += dp[i][j] * (n_all_cands - n_bridges[j])
                dp[i + 1][j + 1] += dp[i][j] * n_bridges[j]
            elif j == W - 1:
                dp[i + 1][j] += dp[i][j] * (n_all_cands - n_bridges[j - 1])
                dp[i + 1][j - 1] += dp[i][j] * n_bridges[j - 1]
            else:
                dp[i + 1][j] += dp[i][j] * (n_all_cands - n_bridges[j - 1] - n_bridges[j])
                dp[i + 1][j - 1] += dp[i][j] * n_bridges[j - 1]
                dp[i + 1][j + 1] += dp[i][j] * n_bridges[j]

    return dp[-1][K - 1] % (10**9 + 7)


print((main()))
