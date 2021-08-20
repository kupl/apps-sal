def f_knapsack_for_all_subsets_power_series(MOD=998244353, MAX=3010):
    import numpy as np
    (N, S) = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    f = np.zeros(MAX + 1, np.int64)
    f[0] = 1
    for a in A:
        f_next = 2 * f
        f_next[a:] += f[:-a]
        f_next %= MOD
        f = f_next
    return f[S]


print(f_knapsack_for_all_subsets_power_series())
