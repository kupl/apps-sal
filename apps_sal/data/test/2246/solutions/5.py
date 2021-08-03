import sys
from collections import deque
def read(): return sys.stdin.readline().rstrip()
def readi(): return int(sys.stdin.readline())
def writeln(x): return sys.stdout.write(str(x) + "\n")
def write(x): return sys.stdout.write(x)


N = readi()
if N == 1:
    writeln(0)
    return

G = [set() for _ in range(N)]
for _ in range(N - 1):
    u, v = list(map(int, read().split()))
    G[u - 1].add(v - 1)
    G[v - 1].add(u - 1)

visited = [0] * N
prev = [0] * N
visited[0] = 1
prev[0] = 1
q = deque([0])
lengths = []
ev = 0
while q:
    cur = q.popleft()
    n_neighbor = len(G[cur])
    if cur == 0:
        divs = n_neighbor
    else:
        divs = n_neighbor - 1
    if n_neighbor == 1 and cur != 0:
        ev += (visited[cur] - 1) * prev[cur]
        continue

    for nxt in G[cur]:
        if not visited[nxt]:
            visited[nxt] = visited[cur] + 1
            prev[nxt] = (1 / divs) * prev[cur]
            q.append(nxt)

print('%.12f' % ev)
