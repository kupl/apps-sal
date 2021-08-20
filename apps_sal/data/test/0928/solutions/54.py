import numpy as np
(N, K) = list(map(int, input().split()))
a = list(map(int, input().split()))
a.insert(0, 0)
Acum = np.array(a).cumsum()
(l, r) = (0, 1)
ans = 0
while True:
    if Acum[r] - Acum[l] < K:
        if r < N:
            r += 1
        else:
            l += 1
    if Acum[r] - Acum[l] >= K:
        ans += len(Acum[r:])
        l += 1
    if l == N:
        break
print(ans)
