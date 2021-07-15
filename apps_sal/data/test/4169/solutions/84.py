# author:  Taichicchi
# created: 12.09.2020 18:05:06

import sys

N, M = list(map(int, input().split()))

ls = []

for i in range(N):
    ls.append(list(map(int, input().split())))

ls.sort(key=lambda x: x[0])

ans = 0

for l in ls:
    if l[1] <= M:
        M -= l[1]
        ans += l[0] * l[1]
    else:
        ans += l[0] * M
        break


print(ans)

