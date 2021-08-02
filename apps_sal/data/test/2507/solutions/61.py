import numpy as np
N, K = map(int, input().split())
As = np.array(sorted(map(int, input().split())))
Fs = np.array(sorted(map(int, input().split()), reverse=True))

times = As * Fs

ng = -1
ok = np.amax(times) + 1

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    k = np.sum(np.maximum(np.ceil((times - mid) / Fs), 0))
    if k > K:
        ng = mid
    else:
        ok = mid

print(ok)
