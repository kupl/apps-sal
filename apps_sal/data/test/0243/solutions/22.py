def put():
    return list(map(int, input().split()))


def find(i):
    if i == p[i]:
        return i
    p[i] = find(p[i])
    return p[i]


def union(i, j):
    if rank[i] < rank[j]:
        (i, j) = (j, i)
    elif rank[i] == rank[j]:
        rank[i] += 1
    p[j] = i
    z[i] += z[j]
    return z[i]


(n, m, k) = put()
l = list(put())
(z, edge, p, rank) = ([0] * (n + 1), [], list(range(n + 1)), [0] * (n + 1))
for i in l:
    z[i] = 1
for i in range(m):
    (u, v, w) = put()
    edge.append((w, u, v))
edge.sort()
for (w, u, v) in edge:
    (u, v) = list(map(find, (u, v)))
    if u != v:
        cnt = union(u, v)
        if cnt == k:
            print((str(w) + ' ') * k)
            break
