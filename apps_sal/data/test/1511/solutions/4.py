n, m, k = map(int, input().split())
cores = [1 for i in range(n)]
cells = [1 for i in range(k)]
info = []
blockings = [0 for i in range(n)]
for i in range(n):
    k = list(map(int, input().split()))
    for j in range(len(k)):
        k[j] -= 1
    info.append(k)
for i in range(m):
    for j in range(n):
        if cores[j] == 0:
            continue
        cell = info[j][i]
        if cell == -1:
            continue
        if cells[cell] == 0:
            cores[j] = 0
            blockings[j] = i + 1
            continue
        for core in range(n):
            if core != j:
                cell_1 = info[core][i]
                if cell_1 == cell and blockings[core] == 0:
                    cells[cell] = 0
                    cores[j] = 0
                    blockings[j] = i + 1
                    break
for elem in blockings:
    print(elem)
