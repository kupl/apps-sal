n, m = map(int, input().split())
NINF = -10**20
edge = []
dist = [NINF] * n
dist[0] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    edge.append((a - 1, b - 1, c))
for i in range(n):
    for a, b, c in edge:
        if dist[a] != NINF and dist[b] < dist[a] + c:
            dist[b] = dist[a] + c
            if i == n - 1 and b == n - 1:
                print('inf')
                return
print(dist[-1])
