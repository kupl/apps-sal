# author:  Taichicchi
# created: 16.09.2020 23:07:07

import sys

N, M = list(map(int, input().split()))

k = []
s = []

for i in range(M):
    _k, *_s = list(map(int, input().split()))
    k.append(_k)
    s.append(_s)

p = list(map(int, input().split()))
ans = 0


for i in range(2 ** N):
    sw = [0 for _ in range(N)]
    for j in range(N):
        if i >> j & 1:
            sw[j] = 1

    for m in range(M):
        mod = 0
        for switch in s[m]:
            mod += sw[switch - 1]
        if mod % 2 != p[m]:
            break
    else:
        ans += 1

print(ans)

