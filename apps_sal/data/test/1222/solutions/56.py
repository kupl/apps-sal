# !/usr/bin/env python3
# from heapq import *
#
# a = [*range(1, 10)]
# heapify(a)
# i = 0
# k = int(input())
# c = 0
# while True:
#    t = str(heappop(a))
#    i += 1
#    if i == k:
#        break
#    if t[-1] != "0":
#        heappush(a, int(t + str(int(t[-1]) - 1)))
#    heappush(a, int(t + t[-1]))
#    if t[-1] != "9":
#        heappush(a, int(t + str(int(t[-1]) + 1)))
# print(t)

from collections import deque

a = deque(list(range(1, 10)))
for _ in range(int(input())):
    i = a.popleft()
    m = i % 10
    i = 10 * i + m
    if m > 0:
        a.append(i - 1)
    a.append(i)
    if m < 9:
        a.append(i + 1)
print((i // 10))

