N, M = map(int, input().split())
road = []
for i in range(M):
    a, b, c = map(int, input().split())
    road.append((a - 1, b - 1, -c))

INF = 10**15
d = [INF] * N
d[0] = 0


def bellman_ford():
    nonlocal d
    for i in range(N):
        for a, b, c in road:
            d[b] = min(d[b], d[a] + c)


bellman_ford()
for a, b, c in road:
    new_d = d[a] + c
    if new_d < d[b]:
        d[b] = - float('inf')

bellman_ford()
if d[-1] > -float('inf'):
    print(int(-d[-1]))
else:
    print('inf')
