import numpy as np
(N, K) = list(map(int, input().split()))
H = [int(input()) for _ in range(N)]
sH = np.array(sorted(H), dtype=np.int64)
shift = sH[K - 1:]
diff = shift - sH[:len(shift)]
ans = min(diff)
print(ans)
