#! /usr/bin env python3
# -*- coding:utf-8 -*-

n = int(input())
data = list(map(int, input().split())) + [0, ]

ans, inc, dec = [0] * n, -1, 1e7
for i in range(n):
    if inc < data[i] < dec:
        if data[i] < data[i + 1]:
            inc = data[i]
        else:
            dec = data[i]
            ans[i] = 1
    elif inc < data[i]:
        inc = data[i]
    elif dec > data[i]:
        dec = data[i]
        ans[i] = 1
    else:
        print("NO")
        break
else:
    print("YES")
    print(*ans)

