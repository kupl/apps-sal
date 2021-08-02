I = lambda: list(map(int, input().split()))
n = int(input())
permutation = list(I())
components = [-1] * n
matrix = [[int(c) for c in input()] for _ in range(n)]

current = 0


def dfs(i):
    nonlocal current
    if components[i] < 0:
        components[i] = current
        for j, b in enumerate(matrix[i]):
            if(b):
                dfs(j)


for i in range(n):
    dfs(i)
    current += 1

slots = [components[i] for i in range(n)]

groups = []
for i in range(current):
    groups.append(sorted([permutation[j] for j in range(n) if components[j] == i]))

pretty = []
for p in slots:
    pretty.append(str(groups[p][0]))
    groups[p] = groups[p][1:]
print(' '.join(pretty))
