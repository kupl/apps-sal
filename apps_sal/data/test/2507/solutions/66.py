import numpy as np
(N, K) = map(int, input().split())
As = np.sort(list(map(int, input().split())))
Fs = np.sort(list(map(int, input().split())))[::-1]
l = As * Fs
left = 0
right = max(l)
while right - left >= 1:
    mid = left + (right - left) / 2
    if np.maximum(As - mid // Fs, 0).sum() <= K:
        right = mid
    else:
        left = mid
print(int(right))
