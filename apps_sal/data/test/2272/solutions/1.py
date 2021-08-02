def DFS(v, b, visited):
    visited.add(v)
    nonlocal count, matrix, ok
    if v == b:
        ok = True
        return
    for i in range(count):
        if matrix[v][i] == 1 and v != i and i not in visited:
            DFS(i, b, visited)


n = int(input())
matrix = [[0] * 111 for i in range(111)]
count = 0
ok = False
intervals = []
for i in range(n):
    t, a, b = list(map(int, input().split()))
    if t == 1:
        intervals.append((a, b))
        for l in range(count):
            c, d = intervals[l]
            if c < a < d or c < b < d:
                matrix[count][l] = 1
            if a < c < b or a < d < b:
                matrix[l][count] = 1
        count += 1
    if t == 2:
        visited = set()
        ok = False
        res = DFS(a - 1, b - 1, visited)
        if ok: print("YES")
        else: print("NO")
