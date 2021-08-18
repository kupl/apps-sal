from collections import deque
n = int(input())
adj = [[] for _ in range(n)]

for _ in range(n - 1):
    u, v = list(map(int, input().split()))
    adj[u - 1].append(v - 1)
    adj[v - 1].append(u - 1)


def bfs(v):
    vis = [i == v for i in range(n)]
    paths = deque([[v]])

    while paths:
        p = paths.popleft()
        for nv in adj[p[-1]]:
            if not vis[nv]:
                vis[nv] = True
                paths.append(p + [nv])

    return p


diameter = bfs(0)
diameter = bfs(diameter[-1])
p = diameter[len(diameter) // 2]

start = (0, 0)
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def gpt(pt, i, dis): return (pt[0] + move[i][0] * dis, pt[1] + move[i][1] * dis)


vis = [False] * n
dis = 2 ** (len(diameter) + 1)

ans = [0] * n
q = deque([(p, start, -1, dis)])

while q:
    p, start, dr, dis = q.popleft()
    vis[p] = True
    ans[p] = start

    if len(adj[p]) > 4:
        print("NO")
        return

    if dr == -1:
        drs = [i for i in range(4)]
    else:
        drs = [i for i in range(4) if gpt(move[i], dr, 1) != (0, 0)]

    for nv in adj[p]:
        if not vis[nv]:
            vis[nv], dr = True, drs.pop()
            npt = gpt(start, dr, dis)
            q.append((nv, npt, dr, dis // 2))
            ans[nv] = npt

print("YES")
for pt in ans:
    print(*pt)
