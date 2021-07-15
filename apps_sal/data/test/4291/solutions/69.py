# author:  Taichicchi
# created: 26.09.2020 13:43:12

import sys

N, Q = map(int, input().split())

S = input()

ls = [0]

for i in range(N):
    if i == 0:
        ls.append(0)
    else:
        if S[i - 1:i + 1] == "AC":
            ls.append(ls[-1] + 1)
        else:
            ls.append(ls[-1])

for q in range(Q):
    l, r = map(int, input().split())

    print(ls[r] - ls[l])
