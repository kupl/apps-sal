n = int(input().strip())

parent = [None for i in range(n + 1)]
children = [[] for i in range(n + 1)]
cs = [None for i in range(n + 1)]

for i in range(1, n + 1):
    p, c = list(map(int, input().split()))
    parent[i] = p
    if p != -1:
        children[p].append(i)
    cs[i] = c

# print(parent)
# print(children)
# print(cs)

to_delete = []
for i in range(1, n + 1):
    if parent[i] > 0 and cs[i] == 1 and sum([cs[item] for item in children[i]]) == len(children[i]):
        to_delete.append(i)

if len(to_delete) > 0:
    print(' '.join([str(item) for item in to_delete]))
else:
    print(-1)
