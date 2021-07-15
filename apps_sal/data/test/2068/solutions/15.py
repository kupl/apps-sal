deep = dict()
n = int(input())
adj_dict = dict()
for i in range(n):
    line = [s.lower() for s in input().split()]
    name1 = line[0]
    name2 = line[2]
    if name2 not in list(adj_dict.keys()):
        adj_dict[name2] = list()
        adj_dict[name2].append(name1)
    else:
        adj_dict[name2].append(name1)
    deep[name1] = 0
    deep[name2] = 0
queue = list()
queue.append('polycarp')
while queue:
    current = queue[0]
    queue = queue[1:]
    if current not in adj_dict:
        continue
    for nei in adj_dict[current]:
        deep[nei] = deep[current] + 1
        queue.append(nei)

print(max(deep.values()) + 1)

