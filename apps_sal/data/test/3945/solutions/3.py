n, m = (int(x) for x in input().split())

field = [[int(x) for x in input().split()] for _ in range(n)]

r_c___rord = []
r_c___cord = [[] for _ in range(n)]

r___uniques_nr = []
c___uniques_nr = []

for r in range(n):
    row = field[r]
    srted = sorted(list(set(row)))
    r___uniques_nr.append(len(srted))
    srted = {x: i for i, x in enumerate(srted)}
    ords = [srted[x] for x in row]
    r_c___rord.append(ords)

for c in range(m):
    col = [field[i][c] for i in range(n)]
    srted = sorted(list(set(col)))
    c___uniques_nr.append(len(srted))
    srted = {x: i for i, x in enumerate(srted)}
    ords = [srted[x] for x in col]
    for i in range(n):
        r_c___cord[i].append(ords[i])

for r in range(n):
    curr = []
    for c in range(m):
        less_nr = max(r_c___rord[r][c], r_c___cord[r][c])
        greq_nr = max(r___uniques_nr[r] - r_c___rord[r][c], c___uniques_nr[c] - r_c___cord[r][c])
        curr.append(less_nr + greq_nr)
    print(*curr)
