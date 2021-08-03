#!/usr/bin/env python3

N, M = list(map(int, input().split()))
h_list = list(map(int, input().split()))
h_dict = {i + 1: h for i, h in enumerate(h_list)}
h_set = set(h_dict.keys())
no_list = []

for _ in range(M):
    a, b = list(map(int, input().split()))
    if h_dict[a] == h_dict[b]:
        no_list.append(a)
        no_list.append(b)
    elif h_dict[a] > h_dict[b]:
        no_list.append(b)
    else:
        no_list.append(a)

no_set = set(no_list)
ans = len(h_set - no_set)

print(ans)
