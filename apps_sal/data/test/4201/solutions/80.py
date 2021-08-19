from itertools import product
import numpy as np

H, W, K = list(map(int, input().split()))
C = []
for _ in range(H):
    tmp = [m for m in map(str, input())]
    C.append(tmp)

C = np.array(C)

ans = 0
for h in product(list(range(2)), repeat=H):
    for w in product(list(range(2)), repeat=W):

        cnt = 0
        for ih in range(H):
            for iw in range(W):
                if C[ih, iw] == '#' and (h[ih] and w[iw]):
                    cnt += 1

        if cnt == K:
            ans += 1

print(ans)
