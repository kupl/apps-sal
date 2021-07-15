# -*- coding: utf-8 -*-

N,M = map(int, input().split())
load_num = [0] * N
for i in range(M):
    a, b = map(int, input().split())
    load_num[a-1] += 1
    load_num[b-1] += 1

for i in range(N):
    print(load_num[i])
