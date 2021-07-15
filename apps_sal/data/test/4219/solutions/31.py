# -*- coding: utf-8 -*-

N = int(input())

A = []
data = []
for i in range(N):
    a = int(input())
    A.append(a)
    x = [list(map(int, input().split())) for _ in range(a)]
    data.append(x)

ans = 0
for i in range(1<<N):
    bit = [0] * N
    cnt = 0
    for j in range(N):
        div = 1 << j
        bit[j] = (i // div) % 2
        if bit[j] == 1:
            cnt += 1

    flag = True
    for j in range(N):
        if bit[j] == 0:
            continue
        for a in range(A[j]):
            x = data[j][a]
            if bit[x[0]-1] != x[1]:
                flag = False
                break
        if not flag:
            break
    
    if flag:
        ans = max(ans, cnt)

print(ans)


