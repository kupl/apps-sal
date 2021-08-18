

import math


n = int(input())
data = list(input())


firstsilver = -1
secondsilver = -1
mdiff = [-1, -1, -1]

for i in range(0, n):
    if data[i] == 'S' and secondsilver == -1:
        secondsilver = i
    elif data[i] == "S":
        firstsilver = secondsilver
        secondsilver = i
    diff = i - firstsilver
    if diff > mdiff[0]:
        mdiff = [diff, firstsilver, i, secondsilver]


if mdiff[1] == mdiff[3]:
    penalty = 0
else:
    penalty = 1

for i in range(0, n):
    if i not in list(range(mdiff[1] + 1, mdiff[2] + 1)):
        if data[i] == 'G':
            penalty = 0


print(mdiff[0] - penalty)
