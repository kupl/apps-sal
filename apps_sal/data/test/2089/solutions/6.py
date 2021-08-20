from queue import Queue


def BFS(v):
    used = {k: -1 for k in range(1, n + 1)}
    st = Queue()
    st.put(v)
    used[v] = 0
    while not st.empty():
        u = st.get()
        for v in range(1, n + 1):
            if graph[u][v] and used[v] == -1:
                used[v] = used[u] + 1
                st.put(v)
    return used


(n, m, s, t) = list(map(int, input().split()))
graph = {k: {k_: False for k_ in range(1, n + 1)} for k in range(1, n + 1)}
for i in range(m):
    (a, b) = list(map(int, input().split()))
    graph[a][b] = True
    graph[b][a] = True
S = BFS(s)
T = BFS(t)
ro = S[t]
ans = 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a != b and (not graph[a][b]) and (S[a] + T[b] + 1 >= ro) and (S[b] + T[a] + 1 >= ro):
            ans += 1
print(ans // 2)
