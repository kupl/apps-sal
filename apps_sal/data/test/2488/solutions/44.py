import math
from bisect import bisect_right

n, d, a = map(int, input().split())
x_list = []
max_x = 0
for _ in range(n):
    x, h = map(int, input().split())
    x -= 1
    x_list.append([x, h])
    max_x = max(max_x, x)
x_list.sort()
xx = [x[0] for x in x_list]
hh = [x[1] for x in x_list]
ans = 0
accum = [0 for _ in range(n)]
for index, [x, h] in enumerate(x_list):
    if index != 0:
        accum[index] += accum[index - 1]
    cnt = max(math.ceil((hh[index] - accum[index]) / a), 0)
    ans += cnt
    index_right = bisect_right(xx, xx[index] + (2 * d))
    accum[index] += cnt * a
    if index_right < n:
        accum[index_right] -= cnt * a
print(ans)
