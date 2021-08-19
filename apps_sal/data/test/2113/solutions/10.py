def input_numbers():
    return list(map(int, input().split()))


n = int(input())
g = {}
i = 1
while i <= n:
    g[i] = set()
    i += 1
i = 1
while i <= n - 1:
    (u, v) = input_numbers()
    g[u].add(v)
    g[v].add(u)
    i += 1
queue = [1]
visited = set()
part1 = set(queue)
part2 = set()
while len(queue):
    u = queue.pop(0)
    visited.add(u)
    for v in g[u]:
        if v not in visited:
            queue.append(v)
            if u in part1:
                part2.add(v)
            else:
                part1.add(v)
need = len(part1) * len(part2) - (n - 1)
print(need)
