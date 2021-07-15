from collections import defaultdict

adj_matrix = defaultdict(list)

n = int(input())
s1 = input()
s2 = input()

#Create Graph
for i in range(n):
    if(s1[i] != s2[i]):
        adj_matrix[s1[i]].append(s2[i])
        adj_matrix[s2[i]].append(s1[i])

visited = set()
mst = []
count = 0
def dfs_util(vertices):
    nonlocal  count
    for vertex in adj_matrix[vertices]:
        if vertex not in visited:
            count += 1
            mst.append((vertices, vertex))
            visited.add(vertex)
            dfs_util(vertex)

for vertices in adj_matrix:
    if vertices not in visited:
        visited.add(vertices)
        dfs_util(vertices)
print(count)
for finds in mst:
    print(finds[0], finds[1])
