from collections import deque
n = int(input())


def R():
    return list(map(int, input().split()))


p = []
w = {}
r = {}
pr = {}
for _ in range(n):
    (x, y) = R()
    p.append((x, y))
p = sorted(p)
for (i, wi) in enumerate(list(R()), 1):
    if wi not in w:
        w[wi] = deque()
    w[wi].append(i)


def solve(p, w, r):
    for i in range(len(p)):
        d = p[i][1] - p[i][0]
        if d in w:
            q = w[d]
            if len(q) > 0:
                ind = q.popleft()
                r[ind] = p[i]
                pr[p[i]] = ind
                if not check_neighbours(p[i], ind, pr):
                    return 0
            else:
                return 0
        else:
            return 0
    return 1


def check_neighbours(p, ind, pr):
    n1 = (p[0] - 1, p[1])
    n2 = (p[0], p[1] - 1)
    n3 = (p[0] - 1, p[1] - 1)
    return check_neighbour(n1, ind, pr) and check_neighbour(n2, ind, pr) and check_neighbour(n3, ind, pr)


def check_neighbour(nb, ind, pr):
    if nb in pr:
        if pr[nb] > ind:
            return 0
    return 1


if solve(p, w, r) == 0:
    print('NO')
else:
    print('YES')
    for (k, v) in sorted(r.items()):
        print(v[0], v[1])
