def I(): return list(map(int, input().split()))


n = int(input())
permutation = list(I())


def row(): return [int(c) for c in input()]


matrix = [row() for _ in range(n)]
components = [-1] * n


def dfs(i):
    nonlocal current
    if components[i] < 0:
        components[i] = current
        row = enumerate(matrix[i])
        row = [j for j, a in row if a > 0]
        for x in row:
            dfs(x)


current = 0
for i in range(n):
    dfs(i)
    current += 1

groups = []
for i in range(current):
    indices = [j for j, c in enumerate(components) if c == i]
    groups.append(sorted([permutation[j] for j in indices]))

pretty = []
for p in components:
    pretty.append(str(groups[p][0]))
    groups[p] = groups[p][1:]
print(' '.join(pretty))
