import numpy as np
N,K = list(map(int,input().split()))
MOD = 10 ** 9 + 7
M = int(N**.5)

# M+1以上で、商がぢょうとxになるやつ
upper_cnt = np.zeros(M+1, dtype=np.int64)
a = np.arange(M+1, dtype=np.int64)
upper_cnt[1:] = N // a[1:] - np.maximum(M, N // (a[1:]+1))

# 数列の末端ごとの個数
# upperについては、個数にわたって合計をとる
lower = np.zeros(M+1, dtype=np.int64)
upper = np.zeros(M+1, dtype=np.int64)
# 0項目に1を置いておくとする
lower[1] = 1
for k in range(1,K+1):
    prev_lower = lower
    prev_upper = upper
    np.cumsum(prev_lower, out = prev_lower)
    np.cumsum(prev_upper, out = prev_upper)
    prev_lower %= MOD
    prev_upper %= MOD
    # 下側 to 下側
    lower = np.zeros(M+1, dtype=np.int64)
    lower += (prev_lower[-1] + prev_upper[-1])
    lower[1:] -= prev_upper[:-1] # 商がn-1以下だと受け付けない
    lower[0] = 0
    # 上側 to 上側：ないはず
    # 下側 to 上側：
    upper = prev_lower * upper_cnt
    lower %= MOD
    upper %= MOD
    
answer = (lower.sum() + upper.sum()) % MOD
print(answer)

