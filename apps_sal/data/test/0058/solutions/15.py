#!/usr/bin/env python3
# Door Frames
n = int(input())
a = int(input())
b = int(input())

res = [[0 for i in range(5)] for j in range(3)]
size = [[0 for i in range(5)] for j in range(3)]


def get_max_size(i, j):
    u = size[j - 1][i] if j else 0
    l = size[j][i - 1] if i else 0
    ru = res[j - 1][i] if j else i
    rl = res[j][i - 1] if i else j
    if u - b >= 0:
        du = u - b
        dru = 0
    else:
        du = n - b
        dru = 1

    if l - a >= 0:
        dl = l - a
        drl = 0
    else:
        dl = n - a
        drl = 1

    if (ru + dru) < (rl + drl):
        return (ru + dru), du
    elif (ru + dru) > (rl + drl):
        return (rl + drl), dl
    elif du > dl:
        return (ru + dru), du
    else:
        return (rl + drl), dl


for j in range(3):
    for i in range(5):
        if (i + j):
            r, m = get_max_size(i, j)
            res[j][i] = r
            size[j][i] = m

print(res[-1][-1])
