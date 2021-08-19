from collections import defaultdict, deque
MOD = 10 ** 9 + 7


def bfs(v):
    q.append(v)
    visited[v] = True
    while q:
        s = q.popleft()
        b.append(v)
        for i in g[s]:
            if not visited[i[0]] and i[1] == 0:
                q.append(i[0])
                visited[i[0]] = True


(n, k) = list(map(int, input().split()))
g = defaultdict(list)
for _ in range(n - 1):
    (x, y, c) = list(map(int, input().split()))
    g[x].append((y, c))
    g[y].append((x, c))
visited = [False] * (n + 1)
count = 0
ans = pow(n, k, MOD)
q = deque()
for i in range(1, n + 1):
    b = []
    if visited[i] == False:
        bfs(i)
    f = len(b)
    count = (count + pow(f, k, MOD)) % MOD
ans = (ans - count) % MOD
print(ans)
