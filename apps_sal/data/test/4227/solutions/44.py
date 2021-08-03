from collections import defaultdict
N, M = list(map(int, input().split()))
d = defaultdict(list)
for _ in range(M):
    a, b = list(map(int, input().split()))
    d[a].append(b)
    d[b].append(a)


def dfs(n, path):
    count = 0
    path.append(n)
    if len(path) == N:
        count += 1
        return count

    for i in range(len(d[n])):
        if d[n][i] not in path:
            count += dfs(d[n][i], path)
            path.pop()

    return count


print((dfs(1, [])))
