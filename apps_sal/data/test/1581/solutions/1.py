import numpy as np
N, K = tuple(map(int, input().split()))
mod = 1000000007

m = N ** 0.5
cnt = [N // i - N // (i + 1) for i in range(1, int(m) + 1)] 
cnt = np.array((cnt + [1 for _ in range(N - sum(cnt))])[::-1])
nxt = cnt[:]
for _ in range(K - 1):
    cnt = nxt * np.cumsum(cnt)[::-1] % mod

print((sum(cnt) % mod))

