import collections

n = int(input())
route = {i + 1: {} for i in range(n)}
for i in range(n - 1):
    a, b, c = map(int, input().split())
    route[a][b] = c
    route[b][a] = c
q, k = map(int, input().split())
queue = collections.deque([k])
length = [0] * (n + 1)
while queue:
    search = queue.popleft()
    pairs = []
    for i, j in route[search].items():
        queue.append(i)
        length[i] = length[search] + j
        pairs.append([search, i])
    for i, j in pairs:
        del route[i][j]
        del route[j][i]
for i in range(q):
    x, y = map(int, input().split())
    print(length[x] + length[y])
