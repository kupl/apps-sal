(n, m) = list(map(int, input().split()))
G = [list() for i in range(n + 1)]
colored = [False] * (n + 1)
hhog_tail = [1] * (n + 1)
spine_count = [0] * (n + 1)


def find_best_hhog_tail(z):
    if colored[z]:
        return
    colored[z] = True
    for y in G[z]:
        if not colored[y]:
            find_best_hhog_tail(y)
        hhog_tail[z] = max(hhog_tail[z], 1 + hhog_tail[y])


for i in range(m):
    (u, v) = list(map(int, input().split()))
    G[u].append(v) if u > v else G[v].append(u)
    spine_count[u] += 1
    spine_count[v] += 1
for i in range(1, n + 1):
    find_best_hhog_tail(i)
print(max([spine_count[i] * hhog_tail[i] for i in range(1, n + 1)]))
