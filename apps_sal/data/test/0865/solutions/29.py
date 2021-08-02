def knapsack_DP(N, W, weight, value):
    import numpy as np
    dishes = [(weight[i], value[i]) for i in range(N)]
    dishes = sorted(dishes, key=lambda x: x[0])
    dp = np.zeros(W, dtype=int)
    ans = 0
    for w, v in dishes:
        ans = max(dp[-1] + v, ans)
        np.maximum(dp[:-w] + v, dp[w:], out=dp[w:])
    return ans


def __starting_point():
    N, W = map(int, input().split())
    weight = []
    value = []
    for i in range(N):
        w, v = map(int, input().split())
        weight.append(w)
        value.append(v)
    print(knapsack_DP(N, W, weight, value))


__starting_point()
