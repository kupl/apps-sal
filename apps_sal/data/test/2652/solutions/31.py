from heapq import heappop, heappush, heapify
import sys
sys.setrecursionlimit(10 ** 6)
icase = 0
if icase == 0:
    n = int(input())
    xy = [[0] * 2 for i in range(n)]
    x = [0] * n
    y = [0] * n
    for i in range(n):
        (x[i], y[i]) = list(map(int, input().split()))
elif icase == 1:
    n = 3
    x = [1, 3, 7]
    y = [5, 9, 8]
elif icase == 2:
    n = 6
    x = [8, 4, 12, 18, 13, 7]
    y = [3, 9, 19, 1, 5, 6]
xi = [[0] * 2 for i in range(n)]
yi = [[0] * 2 for i in range(n)]
for i in range(n):
    xi[i] = [x[i], i]
    yi[i] = [y[i], i]
xi.sort()
x = xi
y = yi.sort()
y = yi
pair_lst = [i for i in range(n)]
que = []
for i in range(n - 1):
    wi = x[i + 1][0] - x[i][0]
    heappush(que, (wi, x[i][1], x[i + 1][1]))
    wi = y[i + 1][0] - y[i][0]
    heappush(que, (wi, y[i][1], y[i + 1][1]))


def find(x):
    if x == pair_lst[x]:
        return x
    else:
        tmp = find(pair_lst[x])
        pair_lst[x] = tmp
        return tmp


icnt = 0
length_sum = 0
while que:
    (w, s, t) = heappop(que)
    root_s = find(s)
    root_t = find(t)
    if root_s != root_t:
        pair_lst[root_s] = root_t
        length_sum += w
        icnt += 1
print(length_sum)
