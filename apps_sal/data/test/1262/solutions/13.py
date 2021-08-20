n = int(input())
cord = [[*map(int, input().split())] for _ in range(n)]
c = [*map(int, input().split())]
k = [*map(int, input().split())]
plant = set()
covered = set()
parent = [-1] * n
sum = 0
for _ in range(n):
    (cost, idx) = min(([cost, idx] for (idx, cost) in enumerate(c) if idx not in covered))
    sum += cost
    covered.add(idx)
    if parent[idx] == -1:
        plant.add(idx)
    for i in range(n):
        if i in covered:
            continue
        c_l = (k[i] + k[idx]) * (abs(cord[i][0] - cord[idx][0]) + abs(cord[i][1] - cord[idx][1]))
        if c_l < c[i]:
            c[i] = c_l
            parent[i] = idx
print('{}\n{}'.format(sum, len(plant)))
print(*map(lambda x: x + 1, plant))
links = 0
out = ''
for (i, _) in enumerate(parent):
    if _ != -1:
        links += 1
        out += '\n' + str(_ + 1) + ' ' + str(i + 1)
print(links, out)
