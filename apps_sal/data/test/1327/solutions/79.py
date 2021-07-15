#!/usr/bin/env python3
n, m = list(map(int, input().split()))
x, y, z = [0] * n, [0] * n, [0] * n
for i in range(n):
    x[i], y[i], z[i] = list(map(int, input().split()))
ans = -(10 ** 9)
for i in range(8):
    # a,b,c それぞれ正負どちらに合わせるかを決める
    sort = []
    bit = [-1, -1, -1]
    if i % 2:
        bit[0] = 1
    if (i // 2) % 2:
        bit[1] = 1
    if (i // 4) % 2:
        bit[2] = 1
    for i in range(n):
        sort.append(x[i] * bit[0] + y[i] * bit[1] + z[i] * bit[2])
    sort.sort()
    ans = max(ans, sum(sort[n - m :]))
print(ans)

