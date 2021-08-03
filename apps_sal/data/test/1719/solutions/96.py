import collections
import itertools
N = int(input())
mod = 10**9 + 7
dp = collections.defaultdict(int)
dp['TTTA'] = dp['TTTG'] = dp['TTTC'] = dp['TTTT'] = 1
for _ in range(N - 1):
    dp2 = collections.defaultdict(int)
    for p, q, r, s, t in itertools.product('AGCT', repeat=5):
        if 'AGC' in [q + s + t, s + r + t, r + s + t, q + r + t, r + t + s]:
            continue
        else:
            dp2[q + r + s + t] += dp[p + q + r + s] % mod
    dp = dp2
print((sum(dp.values()) % mod))
