#!/usr/bin/env python3
from collections import deque


def search(moji):
    num = len(moji)
    setsn = set([])
    for i in range(len(s)-num+1):
        if s[i:i+num] == moji:
            str_ = s[i:i+num+1]
            if len(str_) == num+1:
                setsn.add(str_)
    sorted_setsn = sorted(setsn, reverse=True)

    return sorted_setsn


s = str(input())
k = int(input())
n = len(s)

sets1 = set([])
for i in range(0, len(s)):
    sets1.add(s[i])

sorted_sets1 = sorted(sets1)

# if k == 1:
#     print(sorted_sets1[0])
#     return
# else:
#     k -= 1

dq = deque(sorted_sets1)

while(len(dq)):
    # print(dq, k)
    moji = dq.popleft()
    k -= 1
    if k == 0:
        print(moji)
        return
    sorted_setsn = search(moji)

    # print(sorted_setsn)
    dq.extendleft(sorted_setsn)

