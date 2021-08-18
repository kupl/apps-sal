

N = int(input())
adj = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)

visited = {0}
cur_level = [0]
levels = []

while cur_level:
    levels.append(cur_level)
    next_level = []
    for n in cur_level:
        for m in adj[n]:
            if m not in visited:
                next_level.append(m)
                visited.add(m)
    cur_level = next_level


color_0 = sum(map(len, levels[0::2]))
color_1 = sum(map(len, levels[1::2]))

out = 0
for i, level in enumerate(levels):
    for n in level:
        if i % 2 == 0:
            out += color_1 - len(adj[n])
        else:
            out += color_0 - len(adj[n])

assert out % 2 == 0
print(out // 2)
