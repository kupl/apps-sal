import sys
input = sys.stdin.readline


n, sx, sy = map(int, input().split())
info = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    info[i][0] -= sx
    info[i][1] -= sy


cnt_1 = 0
cnt_2 = 0
cnt_3 = 0
cnt_4 = 0

for i in range(n):
    if info[i][0] >= 1:
        cnt_1 += 1
    if info[i][1] <= -1:
        cnt_2 += 1
    if info[i][0] <= -1:
        cnt_3 += 1
    if info[i][1] >= 1:
        cnt_4 += 1

max_ = max(cnt_1, cnt_2, cnt_3, cnt_4)
if max_ == cnt_1:
    print(cnt_1)
    print(sx+1, sy)
    return
if max_ == cnt_2:
    print(cnt_2)
    print(sx, sy-1)
    return
if max_ == cnt_3:
    print(cnt_3)
    print(sx-1, sy)
    return
if max_ == cnt_4:
    print(cnt_4)
    print(sx, sy+1)
    return
