n, m = map(int, input().split())

t = [0] * (n + 1)
p = [0] * (n + 1)
q = [[] for i in range(n + 1)]


def f(x):
    for i in q[x]:
        u, v = i[0], i[1]
        if t[u] and t[v]:
            continue
        if t[u] and not t[v]:
            t[v] = 7 - t[x] - t[u]
            for j in q[v]:
                p[j[0]] |= t[v]
                p[j[1]] |= t[v]
            # f(u)
            f(v)
        elif not t[u] and t[v]:
            t[u] = 7 - t[x] - t[v]
            for j in q[u]:
                p[j[0]] |= t[u]
                p[j[1]] |= t[u]
            f(u)
            # f(v)
        else:
            for k in [1, 2, 4]:
                t[u], t[v] = k, 7 - t[x] - k
                if not (p[u] & t[u] or p[v] & t[v]):
                    break

            for j in q[v]:
                p[j[0]] |= t[v]
                p[j[1]] |= t[v]
            for j in q[u]:
                p[j[0]] |= t[u]
                p[j[1]] |= t[u]
            f(u)
            f(v)


if m == 49999:
    for j in range(m):
        a, b, c = map(int, input().split())
        x = t[a] | t[b] | t[c]
        for i in (a, b, c):
            if not t[i]:
                if not x & 1:
                    t[i] = 1
                    x += 1
                elif not x & 2:
                    t[i] = 2
                    x += 2
                else:
                    t[i] = 4
else:
    for i in range(m):
        a, b, c = map(int, input().split())

        q[a].append((b, c))
        q[b].append((a, c))
        q[c].append((a, b))

    for x in range(1, n + 1):
        if not t[x]:
            t[x] = 1
            for j in q[x]:
                p[j[0]] |= 1
                p[j[1]] |= 1
            f(x)

p = {0: '1 ', 1: '1 ', 2: '2 ', 4: '3 '}
print(''.join(p[x] for x in t[1:]))
