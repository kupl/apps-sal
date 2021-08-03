import numpy as np
H, W = map(int, input().split())
Map = [list(input()) for h in range(H)]
Map = [[1 if s == '.' else 0 for s in Map[h]] for h in range(H)]
Map = np.array(Map, dtype=int)
L = Map.copy()
R = Map.copy()
U = Map.copy()
D = Map.copy()
for w in range(1, W):
    L[:, w] = (L[:, w - 1] + 1) * Map[:, w]
    R[:, -(1 + w)] = (R[:, -w] + 1) * Map[:, -(1 + w)]
for h in range(1, H):
    U[h, :] = (U[h - 1, :] + 1) * Map[h, :]
    D[-(1 + h), :] = (D[-h, :] + 1) * Map[-(1 + h), :]
print((L + R + U + D).max() - 3)
