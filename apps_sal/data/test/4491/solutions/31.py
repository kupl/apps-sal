# -*- coding: utf-8 -*-

N = int(input())
A = [list(map(int, input().split())) for _ in range(2)]

ans = 0
for k in range(N):
    res = 0
    for x in range(N):
        if x < k:
            res += A[0][x]
        elif x==k:
            res += A[0][x]+A[1][x]
        else:
            res += A[1][x]

    ans = max(ans,res)

print(ans)
