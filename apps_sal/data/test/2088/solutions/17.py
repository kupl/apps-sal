from bisect import bisect_left as bl, bisect_right as br, insort
import sys
import heapq
from collections import defaultdict as dd, deque
def data(): return sys.stdin.readline().strip()
def mdata(): return map(int, data().split())


mod = int(1e9 + 7)


def bfs(x):
    cnt = 0
    for i in tree[x]:
        bfs(i)
        cnt += a[i]
    if len(tree[x]) == 0:
        cnt = 1
    a[x] = cnt


n = int(data())
tree = [{} for i in range(n)]
if n > 1:
    P = list(mdata())
    for i in range(n - 1):
        tree[P[i] - 1][i + 1] = 0
    a = [0] * n
    for i in range(n - 1, -1, -1):
        if len(tree[i]) == 0:
            a[i] = 1
        else:
            for j in tree[i]:
                a[i] += a[j]
    a.sort()
else:
    a = [1]
print(*a)
