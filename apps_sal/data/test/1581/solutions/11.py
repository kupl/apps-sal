import numpy as np
n, k = list(map(int, input().split()))
mod = 10 ** 9 + 7

m = n ** 0.5
cnt = [n // i - n // (i + 1) for i in range(1, int(m) + 1)] 
cnt = np.array((cnt + [1 for _ in range(n - sum(cnt))])[::-1])
nxt = cnt[:]
for _ in range(k - 1):
	cnt = nxt * np.cumsum(cnt)[::-1] % mod

print((sum(cnt) % mod))

