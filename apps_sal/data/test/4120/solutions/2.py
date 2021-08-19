n, m, k = [int(x) for x in input().split()]
E = [[] for _ in range(n)]
for i in range(m):
    a, b = [int(x) for x in input().split()]
    E[a - 1].append((b - 1, i))
    E[b - 1].append((a - 1, i))


Q = [0]
INFTY = n + 1
levels = [INFTY] * n
levels[0] = 0
E_min = [[] for _ in range(n)]
# bfs
while len(Q) > 0:
    city = Q.pop(0)
    for adj, i in E[city]:
        if levels[city] + 1 <= levels[adj]:
            if levels[adj] == INFTY:
                Q.append(adj)
            levels[adj] = levels[city] + 1
            E_min[adj].append(i)


def gen_poss(city, selected, all_poss, next_choice, poss):
    if len(all_poss) >= k:
        return

    if poss >= k:
        all_poss.append(''.join(selected))
        return

    if city == n:
        all_poss.append(''.join(selected))
    else:
        # choose one from E_min[edge]
        for i in E_min[city]:
            selected[i] = '1'
            next_city = next_choice[city]   # skip edges with only one choice
            gen_poss(next_city, selected, all_poss, next_choice, poss * len(E_min[city]))
            selected[i] = '0'


next_choice = [0] * n
selected = ['0'] * m
nc = n
for i in range(n - 1, -1, -1):
    next_choice[i] = nc
    if len(E_min[i]) > 1:
        nc = i
    if len(E_min[i]) >= 1:
        selected[E_min[i][0]] = '1'
all_poss = []
gen_poss(next_choice[0], selected, all_poss, next_choice, 1)

print('{}\n{}'.format(len(all_poss), '\n'.join(all_poss)))
