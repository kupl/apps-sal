n = int(input())
is_max = list(map(int, input().split()))
parent = list(map(int, input().split()))
adjList = [[] for _ in range(n)]
used = [0] * n
for (v, u) in enumerate(parent):
    adjList[u - 1].append(v + 1)
for i in range(n - 1, 0, -1):
    pi = parent[i - 1] - 1
    if is_max[pi]:
        if used[pi] == 0:
            used[pi] = max(1, used[i])
        else:
            used[pi] = max(1, min(used[pi], used[i]))
    else:
        used[pi] += max(1, used[i])
k = sum([len(adjList[u]) == 0 for u in range(n)])
print(k - used[0] + 1)
