import sys
from itertools import accumulate
(n, m, k, s) = list(map(int, input().split()))
_rate = [list(map(int, input().split())), list(map(int, input().split()))]
rate = [list(accumulate(_rate[0], min)), list(accumulate(_rate[1], min))]
items = [[[0, -1]], [[0, -1]]]
for i in range(m):
    (t, c) = list(map(int, sys.stdin.readline().split()))
    items[t - 1].append([c, i + 1])
items[0].sort()
items[1].sort()
for i in range(2):
    for j in range(1, len(items[i])):
        items[i][j][0] += items[i][j - 1][0]
(ok, ng) = (n, -1)
ans_size = [0, 0]
while abs(ok - ng) > 1:
    mid = ok + ng >> 1
    cnt_1 = min(len(items[0]) - 1, k)
    cnt_2 = k - cnt_1
    while cnt_1 >= 0 and cnt_2 < len(items[1]):
        dollers = items[0][cnt_1][0]
        pounds = items[1][cnt_2][0]
        if dollers * rate[0][mid] + pounds * rate[1][mid] <= s:
            ok = mid
            ans_size = [cnt_1, cnt_2]
            break
        cnt_1 -= 1
        cnt_2 += 1
    else:
        ng = mid
if ok < n:
    print(ok + 1)
    for i in range(2):
        day = 0
        for j in range(0, n):
            if _rate[i][j] == rate[i][ok]:
                day = j + 1
                break
        for j in range(1, ans_size[i] + 1):
            print(items[i][j][1], day)
else:
    print(-1)
