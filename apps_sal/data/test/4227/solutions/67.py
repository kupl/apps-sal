N, M = [int(a) for a in input().split()]


edges = {i: [] for i in range(1, N + 1)}
for i in range(M):
    a, b = [int(a) for a in input().split()]
    edges[a].append(b)
    edges[b].append(a)


def dfs(list):
    if len(list) == N:
        return 1
    else:
        a = list[-1]
        next = [n for n in edges[a] if n not in list]
        if len(next) == 0:
            return 0

        total = 0
        for n in next:
            total += dfs(list + [n])

        return total


ans = dfs([1])

print(ans)
