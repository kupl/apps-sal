(n, q) = map(int, input().split())
graph = [[] for i in range(n)]
for i in range(n - 1):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
weight = [0 for i in range(n)]
for i in range(q):
    (p, x) = map(int, input().split())
    weight[p - 1] += x
st = [0]
visit = [False for i in range(n)]
while not len(st) == 0:
    now = st.pop()
    visit[now] = True
    for e in graph[now]:
        if visit[e]:
            continue
        weight[e] += weight[now]
        st.append(e)
print(' '.join(map(str, weight)))
