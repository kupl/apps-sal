(n, m) = map(int, input().split())
A = set(((i, j) for i in range(2) for j in range(2) if i <= n and j <= m))
A |= set(((n - i, m - j) for i in range(2) for j in range(2) if i <= n and j <= m))
A |= set(((i, m - j) for i in range(2) for j in range(2) if i <= n and j <= m))
A |= set(((n - i, j) for i in range(2) for j in range(2) if i <= n and j <= m))


def dist2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


ans = sorted(((dist2(p1, p2) + dist2(p2, p3) + dist2(p3, p4), p1, p2, p3, p4) for p1 in A for p2 in A for p3 in A for p4 in A if len(set([p1, p2, p3, p4])) == 4))[-1][1:5]
print('\n'.join((str(p[0]) + ' ' + str(p[1]) for p in ans)))
