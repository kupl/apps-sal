from queue import Queue
N = int(input())
G = [[] for _ in range(N)]
Q = [{} for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
    Q[a - 1][b - 1] = i

K = max(list(map(len, G)))
print(K)
ans = [0] * (N - 1)
q = Queue()
q.put(0)
while not q.empty():
    v = q.get()
    c = set()
    for u in G[v]:
        if u < v:
            c.add(ans[Q[u][v]])

    i = 1
    for u in G[v]:
        if u > v:
            while i in c:
                i += 1
            ans[Q[v][u]] = i
            i += 1
            q.put(u)

for a in ans:
    print(a)
