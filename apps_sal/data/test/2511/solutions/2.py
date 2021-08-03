from collections import deque, Counter

N, K, *abf = map(int, open(0).read().split())
ab = [abf[i:i + 2] for i in range(0, len(abf), 2)]
connected = [[] for _ in range(N + 1)]
m = 1000000007
for a, b in ab:
    connected[a].append(b)
    connected[b].append(a)

dist = [-1] * (N + 1)
d = deque([1])
parents = [-1] * (N + 1)
dist[1] = 0
while d:
    temp = d.popleft()
    for edge in connected[temp]:
        if dist[edge] == -1:
            d.append(edge)
            dist[edge] = dist[temp] + 1
            parents[edge] = temp
ans = K
c = Counter(parents)
for x in c.items():
    if x[0] < 1:
        continue
    elif x[0] == 1:
        for i in range(1, x[1] + 1):
            ans = (ans * (K - i)) % m
    else:
        for i in range(2, x[1] + 2):
            ans = (ans * (K - i)) % m
print(ans)
