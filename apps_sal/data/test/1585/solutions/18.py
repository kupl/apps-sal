# author:  Taichicchi
# created: 27.09.2020 23:04:41

import sys

x, y = list(map(int, input().split()))

cnt = 0

while x <= y:
    x *= 2
    cnt += 1

print(cnt)
