from collections import deque

N = int(input())


vlist = [[] for _ in range(N)]

for i in range(N - 1):
    a, b, w = list(map(int, input().split()))
    a -= 1
    b -= 1
    vlist[a].append((b, w))
    vlist[b].append((a, w))

ans = [-1] * N
q = deque()

ans[0] = 0
q.append(0)

while q:
    new = q.popleft()
    for node, weight in vlist[new]:
        if ans[node] != -1:
            continue
        ans[node] = (ans[new] + weight) % 2
        q.append(node)

for i in ans:
    print(i)
