from collections import defaultdict as dd
import math


def nn():
    return int(input())


def li():
    return list(input())


def mi():
    return list(map(int, input().split()))


def lm():
    return list(map(int, input().split()))


(n, k) = mi()
l = lm()
running = [0] * (n - 1)
for i in range(len(l) - 1):
    if i == 0:
        running[i] = (l[i], i + 1)
    else:
        running[i] = (running[i - 1][0] + l[i], i + 1)
running.sort()
sliced = running[:k - 1]
sliced.sort(key=lambda x: x[1])
cost = 0
last = 0
for i in range(len(sliced)):
    cost += (i + 1) * sum(l[last:sliced[i][1]])
    last = sliced[i][1]
cost += k * sum(l[last:])
print(cost)
