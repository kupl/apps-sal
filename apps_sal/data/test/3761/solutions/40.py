# coding:UTF-8
import sys

MOD = 10 ** 9 + 7
INF = float('inf')

S = input()     # 文字列
X, Y = list(map(int, input().split()))     # スペース区切り連続数字

x_num = []
y_num = []
# xs = 0

f = 0
axis = 0
count = 0
for s in S:
    if s == "F":
        count += 1
    else:
        if count > 0:
            if axis == 0:
                if f == 0:
                    # xs = count
                    X -= count
                else:
                    x_num.append(count)
            else:
                y_num.append(count)
            count = 0
        f = 1
        axis = (axis + 1) % 2

if count > 0:
    if axis == 0:
        if f == 0:
            # xs = count
            X -= count
        else:
            x_num.append(count)
    else:
        y_num.append(count)

x_num.sort(reverse=True)
y_num.sort(reverse=True)

xs = X
for x in x_num:
    if xs >= 0:
        xs -= x
    else:
        xs += x

ys = Y
for y in y_num:
    if ys >= 0:
        ys -= y
    else:
        ys += y

if xs == 0 and ys == 0:
    print("Yes")
else:
    print("No")

# dpx = [[0] * (2 * len(S) + 1) for _ in range(len(x_num)+1)]
# dpx[0][xs + len(S)] = 1
# for i in range(1, len(x_num)+1):
#     for j in range(2 * len(S) + 1):
#         if j - x_num[i-1] >= 0 and dpx[i-1][j - x_num[i-1]] == 1:
#             dpx[i][j] = 1
#         if j + x_num[i-1] <= 2 * len(S) and dpx[i-1][j + x_num[i-1]] == 1:
#             dpx[i][j] = 1
#
# dpy = [[0] * (2 * len(S) + 1) for _ in range(len(y_num)+1)]
# dpy[0][len(S)] = 1
# for i in range(1, len(y_num)+1):
#     for j in range(2 * len(S) + 1):
#         if j - y_num[i-1] >= 0 and dpy[i-1][j - y_num[i-1]] == 1:
#             dpy[i][j] = 1
#         if j + y_num[i-1] <= 2 * len(S) and dpy[i-1][j + y_num[i-1]] == 1:
#             dpy[i][j] = 1
#
# if dpx[len(x_num)][X+len(S)] == 1 and dpy[len(y_num)][Y+len(S)] == 1:
#     print("Yes")
# else:
#     print("No")
