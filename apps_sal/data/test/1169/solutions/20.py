import math


def most_edge(n):
    return n * (n - 1) // 2


def can(n, m):
    return most_edge(n) >= m


(n, m) = [int(x) for x in input().split()]
minn = n - 2 * m
minn = max(0, minn)
np = max(0, int(math.sqrt(2 * m)) - 10)
for i in range(np, np + 20):
    if not can(i, m):
        continue
    else:
        maxx = i
        break
maxx = n - maxx
print(minn, maxx)
