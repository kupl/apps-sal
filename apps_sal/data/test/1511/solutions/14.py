def pretty_print_list(a):
    for aa in a:
        print(*aa)


(n, m, k) = map(int, input().split())
x = [[-1 for _ in range(m)] for _ in range(n)]
for i in range(n):
    z = [y for y in map(int, input().split(' '))]
    for j in range(m):
        x[i][j] = z[j]
d = {}
locked_cores = {}
locked_cells = {}
for i in range(m):
    d = {}
    for j in range(n):
        if x[j][i] != 0:
            if not j in locked_cores:
                c = d.get(x[j][i], [])
                c.append(j)
                d[x[j][i]] = c
    for cell in d:
        if len(d[cell]) > 1:
            for core in d[cell]:
                if not core in locked_cores:
                    locked_cores[core] = i + 1
                if not cell in locked_cells:
                    locked_cells[cell] = i + 1
        for core in d[cell]:
            if cell in locked_cells:
                if not core in locked_cores:
                    locked_cores[core] = i + 1
for i in range(n):
    if i in locked_cores:
        print(locked_cores[i])
    else:
        print(0)
