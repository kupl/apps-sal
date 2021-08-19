N = int(input())
tree = [[] for i in range(N)]
for i in range(N - 1):
    (u, v, w) = map(int, input().split())
    tree[u - 1].append((v - 1, w))
    tree[v - 1].append((u - 1, w))
h = []
h.append(0)
distance = [-1 for i in range(N)]
distance[0] = 0
while h:
    k = h.pop(0)
    for v in tree[k]:
        x = v[0]
        y = v[1]
        if distance[x] == -1:
            distance[x] = distance[k] + y
            h.append(x)
for i in range(N):
    if distance[i] % 2 == 0:
        print(0)
    else:
        print(1)
