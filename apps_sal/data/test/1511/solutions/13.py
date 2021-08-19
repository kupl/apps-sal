(n, m, k) = map(int, input().split())
cycles = [[] for x in range(m)]
for x in range(n):
    temp = list(map(int, input().split()))
    for i in range(m):
        cycles[i].append(temp[i])
(active_cores, active_memory) = ([0] * n, [0] * (k + 1))
for i in range(m):
    temp = {}
    for j in range(n):
        if not active_cores[j]:
            temp[cycles[i][j]] = temp.get(cycles[i][j], []) + [j]
    for j in range(n):
        if cycles[i][j] and (not active_cores[j]) and (len(temp[cycles[i][j]]) > 1 or active_memory[cycles[i][j]]):
            active_cores[j] = active_memory[cycles[i][j]] = i + 1
print(*active_cores, sep='\n')
