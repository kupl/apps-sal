from collections import deque
import sys
input = sys.stdin.buffer.readline
inputs = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**9)

n = int(input())
e = [[] for i in range(1 + n)]
ei = {}
for i in range(n - 1):
    """
    e[_].append((__,___))
    e[__].append((_,___))
    """
    _, __ = map(int, input().split())
    e[_].append(__)
    e[__].append(_)
    ei[_, __] = i
    ei[__, _] = i

    """
"""
M = max([len(x)for x in e])
res = [0] * (n - 1)
dq = deque([])
Ms = [1] * (1 + n)
dq.append(1)
while dq:
    now = dq.popleft()
    for ne in e[now]:
        ind = ei[ne, now]
        if res[ind] == 0:
            res[ind] = Ms[now]
            Ms[now] = Ms[now] % M + 1
            Ms[ne] = Ms[now]
            dq.append(ne)
print(M)
print(*res, sep='\n')
