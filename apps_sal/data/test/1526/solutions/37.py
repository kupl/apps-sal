# author:  Taichicchi
# created: 27.09.2020 18:22:26

import sys

ls = list(map(int, input().split()))
ls.sort()
cnt = 0

for i in [0, 1]:
    c = (ls[2] - ls[i]) // 2
    cnt += c
    ls[i] += 2 * c


if (ls[0] == ls[1]) & ((ls[2] - 1) == ls[1]):
    cnt += 1
elif (ls[0] == (ls[2] - 1)) | (ls[1] == (ls[2] - 1)):
    cnt += 2

print(cnt)
