from collections import deque
import sys
from sys import stdin


def I():
    return stdin.readline().rstrip()


def MI():
    return map(int, stdin.readline().rstrip().split())


def LI():
    return list(map(int, stdin.readline().rstrip().split()))

# main part


n, m = MI()

ans = [-1 for _ in range(n + 1)]


ans[0] = 0
ans[1] = 0

V = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = MI()
    V[x].append(y)
    V[y].append(x)

d = deque([1])

while d:
    l = d.popleft()
    for v in V[l]:
        if ans[v] != -1:
            continue
        ans[v] = l
        d.append(v)


if ans.count(-1) > 0:
    print('No')
else:
    print('Yes')
    for i in ans[2:]:
        print(i)
