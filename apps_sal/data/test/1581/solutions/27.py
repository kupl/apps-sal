import numpy as np

MOD = 10**9 + 7


def divisor(x):
    div = [0]
    for i in range(1, int(x**0.5) + 1):
        div.append(i)
        if x != i**2:
            div.append(x // i)
    return div


N, K = map(int, input().split())

div = np.array(divisor(N))
div = np.sort(div)
div_dif = np.diff(div)
div_num = div.size - 1

dp = np.ones((K + 1, div_num), np.int64)

for i in range(K):
    dp[i + 1] = dp[i][::-1] * div_dif % MOD
    dp[i + 1] = dp[i + 1].cumsum() % MOD


print(dp[-1][-1])
