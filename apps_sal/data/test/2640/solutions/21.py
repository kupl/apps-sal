import numpy as np
h, w = map(int, input().split())
grid = np.array([list(input()) for _ in range(h)], dtype="str")

hgrid = np.zeros((h, w), dtype="int")

for hi in range(h):
    hdot = np.array(grid[hi] == ".", dtype="int")
    hgrid[hi] = hgrid[hi-1] * hdot + hdot
    
for hi in range(h-2, -1, -1):
    hi_1 = np.minimum(hgrid[hi+1], hgrid[hi] * hgrid[hi+1])
    hgrid[hi] = np.maximum(hgrid[hi], hi_1)
    
wgrid = np.zeros((h, w), dtype="int")

for wi in range(w):
    wdot = np.array(grid[:, wi] == ".", dtype="int")
    wgrid[:, wi] = wgrid[:, wi-1] * wdot + wdot
    
for wi in range(w-2, -1, -1):
    wi_1 = np.minimum(wgrid[:, wi+1], wgrid[:, wi] * wgrid[:, wi+1])
    wgrid[:, wi] = np.maximum(wgrid[:, wi], wi_1)

print(np.max(wgrid + hgrid) - 1)
