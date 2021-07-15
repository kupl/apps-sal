import numpy as np

def solve(H, W, M, h, w):
    f = [0] * (H+1)
    g = [0] * (W+1)
    for r, c in zip(h, w):
        f[r] += 1
        g[c] += 1
    p = np.max(f)
    q = np.max(g)
    num = len(list(filter(p.__eq__, f))) * len(list(filter(q.__eq__, g)))
    for r, c in zip(h, w):
        if (f[r] == p) and (g[c] == q):
            num -= 1
    return p + q - (num <= 0)

H, W, M = map(int, input().split())
h, w = zip(*[map(int, input().split()) for i in range(M)])
print(solve(H, W, M, h, w))
