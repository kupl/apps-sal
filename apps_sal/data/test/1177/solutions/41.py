import numpy as np
(n, s) = list(map(int, input().split()))
aaa = list(map(int, input().split()))
fwd_acc = np.zeros((n + 1, s + 1), dtype=np.int64)
fwd_acc[0][0] = 1
ans = 0
MOD = 998244353
for (i, a) in enumerate(aaa, start=1):
    fwd_acc[i] = fwd_acc[i - 1]
    fwd_acc[i][0] = i
    if a <= s:
        fwd_acc[i][a:] = fwd_acc[i][a:] + fwd_acc[i][:-a]
    fwd_acc[i] %= MOD
    ans = (ans + fwd_acc[i][s]) % MOD
print(ans)
