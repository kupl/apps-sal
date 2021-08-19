import sys
import math
import collections
import itertools
input = sys.stdin.readline
(N, M) = list(map(int, input().split()))
road = [[] for _ in range(N + 1)]
for _ in range(M):
    (x, y, _) = list(map(int, input().split()))
    road[x].append(y)
    road[y].append(x)
no_visit = set(list(range(1, N + 1)))
q = collections.deque([])
cnt = 0
while no_visit:
    q.append(no_visit.pop())
    cnt += 1
    while q:
        now = q.popleft()
        for nxt in road[now]:
            if nxt in no_visit:
                q.append(nxt)
                no_visit.discard(nxt)
print(cnt)
