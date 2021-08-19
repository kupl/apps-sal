#!/usr/bin/env python3

ss = [input().strip() for _ in range(2)]
n = len(ss[0])

cnt = 0
had1 = False
had2 = False

for i in range(n):
    ccur = sum(s[i] == '0' for s in ss)
    if ccur == 2:
        if had1:
            cnt += 1
            had1 = False
        elif had2:
            cnt += 1
            had2 = False
            had1 = True
        else:
            had2 = True
    elif ccur == 1:
        if had1:
            had1 = True
        elif had2:
            cnt += 1
            had2 = False
        else:
            had1 = True
    else:
        had1 = False
        had2 = False

print(cnt)
