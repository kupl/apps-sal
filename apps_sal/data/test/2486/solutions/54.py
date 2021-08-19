import numpy as np
import itertools

N, K = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()


def check(i):  # i番目のカードを使わなかった時
    dp = np.zeros(K, dtype=np.bool)
    # dp[k]はkが作れる時True
    # 保持する情報はTrue/Falseのみで良いので1次元DPを上書きしていく(1回でまとめて)
    dp[0] = True
    for j in itertools.chain(a[:i], a[i + 1:]):  # i番目の無いカードセット
        dp[j:] = np.logical_or(dp[j:], dp[:-j])  # ある数jを使うと、j以降のもの(N-j)個と前から(N-j)個のどちらかがTrueのものは作れる
    return any(dp[K - a[i]:])  # K-a[i]~K-1のうちどれか作れるならa[i]は必要=True


left = -1
right = N
while right - left > 1:
    mid = (right + left) // 2
    if check(mid):
        right = mid
    else:
        left = mid

print(right)
