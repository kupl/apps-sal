from collections import defaultdict
n, m, k = [int(i) for i in input().split()]
cell = [0 for i in range(k+1)]
core = [0 for i in range(n+1)]

# if core is positive, it has been locked, same if a cell is positive
# core would access the cell

# n is the number of cores
# m is the number of cycle
# k is the number of cells

A = [[int(i) for i in input().split()] for j in range(n)] # reading in the n lines
A = [[0] + [row[i] for row in A] for i in range(len(A[0]))] # now i have tranpose it
# append 0 at the start

# now A is of size m+1 by n
# each row is a timestep

for t in range(m):
    cell_visited = defaultdict(set)
    for i in range(1, n+1): # go through each core
        if A[t][i] > 0 and core[i] == 0: # instruction to do something and the core is not locked
            if cell[A[t][i]] > 0: # the cell is locked, lock the core if it's not locked
                core[i] = t + 1
            elif cell[A[t][i]] == 0: # the cell is not locked
                cell_visited[A[t][i]].add(i)
    for i in cell_visited: #i is the index of the cell
        if len(cell_visited[i]) > 1:
            cell[i] = 1 # lock the cell
            for j in cell_visited[i]:
                core[j] = t + 1
for i in range(1, n+1):
    print(core[i])

