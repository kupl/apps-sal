#!/usr/bin/env python
# -.- coding: utf-8 -.-

lucky = int(input())
lucky = str(lucky)
lenlucky = len(lucky)
acc = 0
acc += 2**(lenlucky) - 1
numindex = [4, 7]
for i in range(lenlucky):
    acc += numindex.index(int(lucky[i])) * 2**(lenlucky - i - 1)
print(acc)

