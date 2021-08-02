from collections import deque
N = int(input())
Edge = [list(map(int, input().strip())) for _ in range(N)]

dist = []
inf = 10**9
for i in range(N):
    d = [inf] * N
    d[i] = 0
    Q = deque([i])
    unused = set(range(N))
    unused.remove(i)
    while Q:
        vn = Q.pop()
        for vf in unused.copy():
            if Edge[vn][vf]:
                unused.remove(vf)
                d[vf] = 1 + d[vn]
                Q.appendleft(vf)
    dist.append(d)

M = int(input())
V = tuple([int(x) - 1 for x in input().split()])

Ans = [V[0]]

for v in V[1:]:
    while len(Ans) > 1 and dist[Ans[-2]][Ans[-1]] + dist[Ans[-1]][v] == dist[Ans[-2]][v]:
        Ans.pop()
    Ans.append(v)

Ans = [a + 1 for a in Ans]
print(len(Ans))
print(*Ans)
