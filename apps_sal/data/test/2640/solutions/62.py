# D - Lamp
import numpy as np

h, w = map(int, input().split())

# 0: 障害物または壁 1: 通路
# 上下左右の壁の分を加味して+2したグリッドを用意する。
g = np.zeros((h + 2, w + 2), dtype=np.int64)
for i in range(h):
    grid = np.array(list(input()))
    g[i + 1, 1:w + 1] = (grid == '.')

# 横について考える
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

# 縦について考える
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

# print(tW)
# print(tH)
print(np.max(tW + tH - 1))


'''
# 横について考える
tblW = np.zeros((h, w),dtype=np.int64)
for i in range(h):
    for j in range(w):
        if grid[i, j]=='#' or tblW[i, j]>0:
            continue
        else:
            cnt = 1
            while j+cnt<w and grid[i, j+cnt]!='#':
                cnt += 1
            tblW[i, j:j+cnt] = cnt
print(tblW)
    
# 縦について考える
tblH = np.zeros((h, w),dtype=np.int64)
for j in range(w):
    for i in range(h):
        if grid[i, j]=='#' or tblH[i, j]>0:
            continue
        else:
            cnt = 1
            while i+cnt<h and grid[i+cnt, j]!='#':
                cnt += 1
            tblH[i:i+cnt, j] = cnt
print(tblH)

ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, tblH[i, j]+tblW[i, j]-1)

print(ans)
'''
