import sys
from collections import defaultdict, deque
def int1(x): return int(x) - 1


read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

N = int(readline())

g = [[] for _ in range(N)]
deg = [0] * N
ab = defaultdict(int)

for _ in range(N - 1):
    a, b = list(map(int1, readline().split()))
    g[a].append(b)
    g[b].append(a)
    deg[a] += 1
    deg[b] += 1
    ab[(a, b)] = -1

color = [-1] * N

print((max(deg)))

C = [0] * N
C[0] = -1

que = deque([0])

while len(que) != 0:
    idx = que.popleft()
    tmp = 1
    for i in g[idx]:
        if C[i] != 0:
            continue
        a, b = idx, i
        if tmp == C[idx]:
            tmp += 1
        ab[(a, b)] = tmp
        C[i] = tmp
        que.append(i)
        tmp += 1

for v in list(ab.values()):
    print(v)
