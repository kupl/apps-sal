n = int(input())
matrix = [[] for i in range(n)]
for i in range(n - 1):
    a = list(map(int, input().split()))
    matrix[a[0]].append([a[1], a[2]])
    matrix[a[1]].append([a[0], a[2]])
way = [float('inf') for i in range(n)]
used = [False for i in range(n)]
v = 0
way[0] = 0
for i in range(n):
    used[v] = True
    for j in matrix[v]:
        way[j[0]] = min(way[j[0]], way[v] + j[1])
    m = float('inf')
    for j in range(n):
        if way[j] < m and not used[j]:
            m = way[j]
            v = j
print(max(way))
