def f_knapsack_for_all_segments(MOD=998244353):
    # 参考: https://maspypy.com/atcoder-参加感想-2019-03-22abc-159
    import numpy as np
    N, S = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]

    ans = 0
    f = np.zeros(S + 1, np.int64)  # f[k]: 多項式の x**k の項の係数
    for a in A:
        # f で表される多項式に対して (f + 1)(1 + x**a) を新しい f とする
        f[0] += 1  # f + 1
        f[a:] += f[:-a].copy()  # 1 + x**a を掛ける
        f %= MOD
        # x**S の項の係数を解に加える
        ans += f[S]
        ans %= MOD
    return ans

print(f_knapsack_for_all_segments())
