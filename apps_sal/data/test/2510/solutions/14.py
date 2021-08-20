from collections import deque


def bfs(edges, start):
    waiting = deque()
    done[start] = 2
    c = 1
    for n in edges[start]:
        done[n] = 1
        waiting.append(n)
    while len(waiting):
        cur_node = waiting.popleft()
        if done[cur_node] != 2:
            done[cur_node] = 2
            c += 1
            for n in edges[cur_node]:
                if done[n] != 2:
                    done[n] = 1
                    waiting.append(n)
    return c


(N, M) = [int(a) for a in input().split()]
edge = [[] for _ in range(N)]
for _ in range(M):
    (a, b) = [int(a) for a in input().split()]
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)
done = [0] * N
ans = 0
for i in range(N):
    if done[i] == 0:
        ans = max(ans, bfs(edge, i))
print(ans)
