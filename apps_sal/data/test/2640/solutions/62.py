import numpy as np
(h, w) = map(int, input().split())
g = np.zeros((h + 2, w + 2), dtype=np.int64)
for i in range(h):
    grid = np.array(list(input()))
    g[i + 1, 1:w + 1] = grid == '.'
gW = np.copy(g)
gW = np.ravel(gW)
tWLeft = np.arange((w + 2) * (h + 2))
tWRight = np.copy(tWLeft)
tWLeft[gW == 1] = 0
tWRight[gW[::-1] == 1] = 0
np.maximum.accumulate(tWLeft, out=tWLeft)
np.maximum.accumulate(tWRight, out=tWRight)
tWRight = len(tWRight) - 1 - tWRight[::-1]
tW = tWRight - tWLeft - 1
tW[gW == 0] = 0
tW = tW.reshape(h + 2, w + 2)
gH = np.copy(g.T)
gH = np.ravel(gH)
tHLeft = np.arange((w + 2) * (h + 2))
tHRight = np.copy(tHLeft)
tHLeft[gH == 1] = 0
tHRight[gH[::-1] == 1] = 0
np.maximum.accumulate(tHLeft, out=tHLeft)
np.maximum.accumulate(tHRight, out=tHRight)
tHRight = len(tHRight) - 1 - tHRight[::-1]
tH = tHRight - tHLeft - 1
tH[gH == 0] = 0
tH = tH.reshape(w + 2, h + 2).T
print(np.max(tW + tH - 1))
"\n# 横について考える\ntblW = np.zeros((h, w),dtype=np.int64)\nfor i in range(h):\n    for j in range(w):\n        if grid[i, j]=='#' or tblW[i, j]>0:\n            continue\n        else:\n            cnt = 1\n            while j+cnt<w and grid[i, j+cnt]!='#':\n                cnt += 1\n            tblW[i, j:j+cnt] = cnt\nprint(tblW)\n    \n# 縦について考える\ntblH = np.zeros((h, w),dtype=np.int64)\nfor j in range(w):\n    for i in range(h):\n        if grid[i, j]=='#' or tblH[i, j]>0:\n            continue\n        else:\n            cnt = 1\n            while i+cnt<h and grid[i+cnt, j]!='#':\n                cnt += 1\n            tblH[i:i+cnt, j] = cnt\nprint(tblH)\n\nans = 0\nfor i in range(h):\n    for j in range(w):\n        ans = max(ans, tblH[i, j]+tblW[i, j]-1)\n\nprint(ans)\n"
