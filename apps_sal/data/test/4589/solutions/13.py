# -*- coding: utf-8 -*-

def get_count(S, H, W, i, j):
    num = 0
    start_i = start_j = -1
    end_i = end_j = 2
    if W == 1:
        start_i = 0 
        end_i = 1
    else:
        if i == 0:
            start_i = 0
        elif i == W-1:
            end_i = 1
    if H == 1:
        start_j = 0
        end_j = 1
    else:
        if j == 0:
            start_j = 0
        elif j == H-1:
            end_j = 1

    for y in range(start_j, end_j, 1):
        for x in range(start_i, end_i, 1):
            if S[j+y][i+x] == "#":
                num += 1

    return num


H,W = list(map(int, input().split()))
S = []
for i in range(H):
    S.append(list(input()))

for y in range(H):
    for x in range(W):
        if S[y][x] == ".":
            num = get_count(S, H, W, x, y)
            S[y][x] = str(num)

for y in range(H):
    print(("".join(S[y])))            

