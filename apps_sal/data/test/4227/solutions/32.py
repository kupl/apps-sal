N, M = [int(a) for a in input().split()]


edges = {i: [] for i in range(1, N + 1)}
for i in range(M):
    a, b = [int(a) for a in input().split()]
    edges[a].append(b)
    edges[b].append(a)


def search(lst):
    if len(lst) == N:
        return 1
    else:
        a = lst[-1]
        next = [n for n in edges[a] if n not in lst]
        if len(next) == 0:
            return 0

        tot = 0
        for n in next:
            tot += search(lst + [n])

        return tot


ans = search([1])

print(ans)
