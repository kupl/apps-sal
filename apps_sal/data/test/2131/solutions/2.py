from copy import deepcopy
import itertools
from bisect import bisect_left


def read():
    return int(input())


def readmap():
    return map(int, input().split())


def readlist():
    return list(map(int, input().split()))


N = read()
degree = [0] * N
for _ in range(N - 1):
    a, b = readmap()
    degree[a - 1] += 1
    degree[b - 1] += 1

more_than_three = 0
for d in degree:
    if d >= 3:
        more_than_three += 1

if more_than_three >= 2:
    print("No")
    quit()

ans = []
if more_than_three == 1:
    for v in range(N):
        if degree[v] >= 3:
            center = v
    for v in range(N):
        if degree[v] == 1:
            ans.append((center + 1, v + 1))
    print("Yes")
    print(len(ans))
    for tup in ans:
        print(tup[0], tup[1])
    quit()

leaf = []
for v in range(N):
    if degree[v] == 1:
        leaf.append(v)
print("Yes")
print(1)
print(leaf[0] + 1, leaf[1] + 1)
