import sys
import numpy as np
input = sys.stdin.readline
n = int(input())
G = np.array([list(map(int, input().split())) for _ in range(n)], dtype=float)
G2 = G
for i in range(n):
    G2[i,i] = np.inf
use = np.ones((n,n),dtype=bool)
impossible = np.zeros((n,n),dtype=bool)
for w in range(n):
    D = sum(np.meshgrid(G2[w], G2[w]))
    use &= ~(G == D)
    impossible |= G > D
if impossible.sum() > n:
    print(-1)
else:
    print(int(np.sum(G[use]) / 2))
