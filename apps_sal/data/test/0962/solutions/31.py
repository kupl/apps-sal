import sys
sys.setrecursionlimit(10**4)


def input():
    return sys.stdin.readline()[:-1]


n, m = map(int, input().split())
adj = [[] for _ in range(n)]
edges = []
for i in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    edges.append((a - 1, b - 1))

seen = [False for _ in range(n)]
visited = [False for _ in range(n)]
begin = -1
hist = []


def dfs(x):
    nonlocal begin, hist
    if begin >= 0:
        return
    seen[x] = True
    hist.append(x)
    for v in adj[x]:
        if visited[v]:
            continue
        if seen[v] == True and visited[v] == False:
            begin = v
            return
        dfs(v)
        if begin >= 0:
            return
    visited[x] = True
    hist.pop()
    return


for i in range(n):
    if begin < 0:
        dfs(i)
    if begin >= 0:
        break

if begin < 0:
    print(-1)
    return
else:
    cycle = []
    included = [False for _ in range(n)]
    included[begin] = True
    while hist and hist[-1] != begin:
        cycle.append(hist[-1])
        included[hist[-1]] = True
        hist.pop()
    cycle.append(begin)
    hist.pop()

    while True:
        meets = True
        l = len(cycle)
        ind = [-1 for _ in range(n)]
        for i in range(l):
            ind[cycle[i]] = i
        for i in range(l):
            if meets == False:
                break
            for v in adj[cycle[(i + 1) % l]]:
                if included[v] == True and v != cycle[i]:
                    meets = False
                    new_start_id, new_end_id = ind[v], (i + 1) % l
                    break

        if meets:
            print(len(cycle))
            print(*[c + 1 for c in cycle], sep="\n")
            break
        else:
            new_cycle = []
            included = [False for _ in range(n)]
            cur = new_end_id
            while cur != new_start_id:
                new_cycle.append(cycle[cur])
                included[cycle[cur]] = True
                cur = (cur + 1) % l
            new_cycle.append(cycle[new_start_id])
            cycle = new_cycle
