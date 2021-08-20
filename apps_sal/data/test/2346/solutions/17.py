n = int(input())
parent_respect = [0] * (n + 1)
graph = [[] for i in range(n + 1)]
root = None
for i in range(1, n + 1):
    (p, r) = [int(j) for j in input().split()]
    if p == -1:
        root = i
        continue
    graph[p].append(i)
    parent_respect[i] = r
result = []
for i in range(1, n + 1):
    if parent_respect[i] == 1:
        all_c_r = False
        for c in graph[i]:
            if parent_respect[c] == 0:
                all_c_r = True
        if not all_c_r:
            result.append(i)
if result:
    for i in result:
        print(i, end=' ')
else:
    print(-1)
