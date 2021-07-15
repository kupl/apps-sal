import queue

q = queue.Queue()
bool = True


def bfs():
    q.put(0)
    while not q.empty():
        now = q.get()
        for i in nodes[now]:
            if dist[i] != -1:
                continue
            dist[i] = dist[now] + 1
            q.put(i)
            ans[i] = now
    # bool = False


N, M = list(map(int, input().split()))
nodes = [[] for i in range(N)]
idxStock = []
for i in range(M):
    a, b = list(map(int, input().split()))
    nodes[a - 1].append(b - 1)
    nodes[b - 1].append(a - 1)

dist = [-1] * N
ans = [-1] * N
bfs()
if bool:
    print("Yes")
    for i in range(1, N):
        print((ans[i] + 1))
else:
    print("No")

