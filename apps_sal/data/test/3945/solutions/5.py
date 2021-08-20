(n, m) = list(map(int, input().split()))
streets = []
for i in range(n):
    streets.append(list(map(int, input().split())))
mem_rows = {}
len_row = []
for i in range(n):
    mem_r = sorted(set(streets[i]))
    srted = {x: i for (i, x) in enumerate(mem_r)}
    ords = [srted[i] for i in streets[i]]
    mem_rows[i] = ords
    len_row.append(len(mem_r))
mem_cols = {}
len_col = []
for j in range(m):
    col = [k[j] for k in streets]
    mem_d = sorted(set(col))
    srted = {x: i for (i, x) in enumerate(mem_d)}
    ords = [srted[i] for i in col]
    mem_cols[j] = ords
    len_col.append(len(mem_d))
for i in range(n):
    prt = []
    for j in range(m):
        elem = streets[i][j]
        (pos1, pos2) = (mem_rows[i][j], mem_cols[j][i])
        streets_ans = max(pos1, pos2) + max(len_row[i] - pos1, len_col[j] - pos2)
        prt.append(streets_ans)
    print(*prt)
