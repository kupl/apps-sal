from collections import defaultdict
n, m, k = [int(i) for i in input().split()]
cell = [0 for i in range(k + 1)]
core = [0 for i in range(n + 1)]


A = [[int(i) for i in input().split()] for j in range(n)]
A = [[0] + [row[i] for row in A] for i in range(len(A[0]))]


for t in range(m):
    cell_visited = defaultdict(set)
    for i in range(1, n + 1):
        if A[t][i] > 0 and core[i] == 0:
            if cell[A[t][i]] > 0:
                core[i] = t + 1
            elif cell[A[t][i]] == 0:
                cell_visited[A[t][i]].add(i)
    for i in cell_visited:
        if len(cell_visited[i]) > 1:
            cell[i] = 1
            for j in cell_visited[i]:
                core[j] = t + 1
for i in range(1, n + 1):
    print(core[i])
