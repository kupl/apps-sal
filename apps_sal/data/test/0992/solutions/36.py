def f_knapsack_for_all_subsets_power_series(MOD=998244353, MAX=3010):
    # 参考: https://maspypy.com/atcoder-参加感想-2020-05-31abc-169
    import numpy as np
    N, S = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]

    f = np.zeros(MAX + 1, np.int64)  # 次数が S より大きな項には興味ないため、こうする
    f[0] = 1  # f_{0}(x) = 1
    for a in A:
        # f_{n+1} = f_{n} * (2 + x**a) = 2 * f_{n} + x**a * f_{n}
        f_next = 2 * f  # 第一項
        f_next[a:] += f[:-a]  # 第二項
        f_next %= MOD
        f = f_next
    return f[S]

print(f_knapsack_for_all_subsets_power_series())
