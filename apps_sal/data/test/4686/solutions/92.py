# -*- coding: utf-8 -*-

S = list(input())
cun = 0
ss = set()

for i in S:
    ss.add(i)

for i in ss:
    cun = 0

    for p in range(len(S)):
        if i == S[p]:
            cun += 1
    if cun % 2 != 0:
        print("No")
        return

print("Yes")
