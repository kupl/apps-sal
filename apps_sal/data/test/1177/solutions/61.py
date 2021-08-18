def f_knapsack_for_all_segments(MOD=998244353):
    import numpy as np
    N, S = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]

    ans = 0
    f = np.zeros(S + 1, np.int64)
    for a in A:
        f[0] += 1
        f[a:] += f[:-a].copy()
        f %= MOD
        ans += f[S]
        ans %= MOD
    return ans


print(f_knapsack_for_all_segments())
