import copy
from itertools import product
import sys
sys.setrecursionlimit(10 ** 6)
(h, w) = list(map(int, input().split()))
map_ = [list(map(int, input().split())) for i in range(10)]
min_ = [[10 ** 4] * 10 for i in range(10)]


def dfs(start=0, now=0, value=0):
    for i in range(10):
        value_tmp = value + map_[now][i]
        if value_tmp < min_[start][i]:
            min_[start][i] = value_tmp
            dfs(start, now=i, value=value_tmp)


for i in range(10):
    dfs(start=i, now=i, value=0)
count = [0] * 10
for i in range(h):
    tmp = list(map(int, input().split()))
    for i in tmp:
        if i != -1:
            count[i] += 1
ans = 0
for i in range(10):
    ans += min_[i][1] * count[i]
print(ans)
