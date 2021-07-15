from sys import exit,stdin,stderr
def rl():
    return [int(w) for w in stdin.readline().split()]

n, m, k = rl()
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = rl()
    adj[u].append(v)
    adj[v].append(u)

layers = [[] for depth in range(k)]
position = [None for _ in range(n + 1)]
layers[0] = [1]
position[1] = (0, None)
for depth in range(1, k):
    for parent in layers[depth - 1]:
        _, gp = position[parent]
        for child in adj[parent]:
            if child == gp:
                continue
            if position[child]:
                depth2, parent2 = position[child]
                path1 = []
                while depth > depth2:
                    path1.append(parent)
                    depth, parent = position[parent]
                path2 = []
                while parent != parent2:
                    path1.append(parent)
                    path2.append(parent2)
                    depth, parent = position[parent]
                    depth2, parent2 = position[parent2]
                path2.reverse()
                path = path1 + [parent] + path2 + [child]
                if len(path) <= k:
                    print(2)
                    print(len(path))
                    print(*path)
                else:
                    print(1)
                    print(*path[:k:2])
                return
            layers[depth].append(child)
            position[child] = depth, parent

print(1)
if layers[k - 1]:
    print(*(layer[0] for layer in layers[::2]))
else:
    k2 = (k + 1) // 2
    r = [[], []]
    for depth, layer in enumerate(layers):
        ri = r[depth % 2]
        ri += layer
        if len(ri) >= k2:
            print(*ri[:k2])
            break

