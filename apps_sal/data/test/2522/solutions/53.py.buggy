#!/usr/bin/env python3

import heapq
import collections
import sys
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
cnt1 = collections.Counter(arr1)
cnt2 = collections.Counter(arr2)
tmp = [[key, cnt1[key]] for key in cnt1.keys()]
tmp = sorted(tmp, reverse=True, key=lambda x: x[1])
arr3 = []
for key, cnt in tmp:
    for _ in range(cnt):
        arr3.append(key)
cnt3 = collections.Counter(arr3)
ans = [0] * n
acum = 0
pos = 0
head = []
tail = []
for key in cnt3.keys():
    tcnt1 = cnt3[key]
    tcnt2 = cnt2[key]
    if tcnt1 + tcnt2 > n:
        print('No')
        return
    acum += tcnt1
    tpos = max(acum, pos)
    remain = tcnt2
    # print(key,blank,remain)
    for i in range(tpos, n):
        if remain == 0:
            break
        ans[i] = key
        remain -= 1
        cnt2[key] -= 1
    for _ in range(remain):
        if tpos != pos:
            head.append(key)
        else:
            tail.append(key)
        cnt2[key] -= 1
    pos = min(tpos + tcnt2, n)
    # print(ans,head,pos)
for key in cnt2.keys():
    if cnt2[key] == 0:
        continue
    for _ in range(cnt2[key]):
        tail.append(key)
pos = 0
head += tail
for i in range(n):
    if ans[i] == 0:
        ans[i] = head[pos]
        pos += 1
q = []
for i in range(n):
    heapq.heappush(q, (arr3[i], ans[i]))
for i in range(n):
    _, val = heapq.heappop(q)
    ans[i] = val
print('Yes')
print(*ans)
