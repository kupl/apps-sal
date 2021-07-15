import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

edges = [[] for _ in range(N)]
for _ in range(M):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    edges[c].append(d)
    edges[d].append(c)

q = deque()
visited = set()
for i in range(N):
    if i in visited:
        continue

    q.append(i)
    a_sum = 0
    b_sum = 0
    while q:
        n = q.popleft()
        if n in visited:
            continue
        visited.add(n)

        a_sum += A[n] 
        b_sum += B[n] 
        for nn in edges[n]:
            q.append(nn)

    if a_sum != b_sum:
        print("No")
        return

print("Yes")
