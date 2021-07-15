from collections import deque

def bfs():
    visit = [0] * (n + 1)
    e = [0] * (m + 1)
    x = [0] * (n + 1)
    q = deque()
    for i in range(1, n + 1):
        if not visit[i]:
            q.append(i)
            visit[i] = 1
            while q:
                j = q.popleft()
                for g in G[j]:
                    if not e[g[2]]:
                        #print(e, visit, q, x, j)
                        e[g[2]] = 1
                        if not visit[g[0]]:
                            x[g[0]] = g[1] + x[j]
                            visit[g[0]] = 1
                            q.append(g[0])
                        else:
                            #print(x[g[0]], g[1] + x[j])
                            if not x[g[0]] == g[1] + x[j]:
                                return False
    return True

n, m = map(int, input().split())
G = [[] for _ in range(n + 1)]
for i in range(m):
    l, r, d = map(int, input().split())
    G[l].append([r, d, i])
    G[r].append([l, -d, i])
print("Yes" if bfs() else "No")
