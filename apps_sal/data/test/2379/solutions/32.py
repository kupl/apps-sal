#!/usr/bin/env python3

# N:全日数 K:働く日数 C:働いた日からその後働かない日数
N, K, C = map(int, input().split())
S = input()

# num回目に働く日はl[num-1]日目以降
l = []
num = 0
i = 0
while num < K:
    if S[i] == "o":
        l.append(i)
        num += 1
        i += C + 1
    else:
        i += 1

# num回目に働く日はl[num-1]日目以前
r = []
num = 0
i = N - 1
while num < K:
    if S[i] == "o":
        r.append(i)
        num += 1
        i -= C + 1
    else:
        i -= 1
r.reverse()

for i in range(K):
    if l[i] == r[i]:
        print(l[i] + 1)
