import sys
import numpy as np
input = sys.stdin.readline
n = int(input())
G = np.array([list(map(int, input().split())) for _ in range(n)], dtype=float)
use = np.ones((n, n), dtype=bool)
impossible = np.zeros((n, n), dtype=bool)
for w in range(n):
    D = sum(np.meshgrid(G[w], G[w]))
    D[w] = np.inf
    D[:, w] = np.inf
    use &= ~(G == D)
    impossible |= G > D
if impossible.any():
    print(-1)
else:
    print(int(np.sum(G[use]) / 2))
