import heapq
import sys
import math
input = sys.stdin.readline


def RI():
    return [int(x) for x in sys.stdin.readline().strip().split()]


def rw():
    return input().strip().split()


infinite = float('inf')
(n, k) = RI()
l = RI()
l.sort()
i = n // 2
median = l[i]
steps = 0
count = 0
while i < n:
    temp = l[i]
    while i < n and l[i] == temp:
        count += 1
        i += 1
    if i < n:
        a = k // count
        if a == 0:
            break
        else:
            diff = l[i] - temp
            if a >= diff:
                k -= diff * count
                median = l[i]
                continue
            else:
                k -= a * count
                median += a
                break
    else:
        a = k // count
        if a == 0:
            break
        else:
            median += a
            break
print(median)
