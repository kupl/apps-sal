c = [[0, 0] for i in range(round(1e6 + 1))]


def ans(t):
    a, k, s = [int(x) for x in input().split()]
    v = list([int(x) for x in input().split()])
    y, x, a, m = 0, 0, 0, 1e12
    for i in range(len(v)):
        if c[v[i]][0] != t:
            c[v[i]] = [t, 0]
        c[v[i]][1] += 1
        if c[v[i]][1] == 1:
            a += 1
        if i - y + 1 > s:
            c[v[y]][1] -= 1
            if c[v[y]][1] == 0:
                a -= 1
            y += 1
        if a < m and i - y + 1 == s:
            m = a
    return m


t = int(input())
for i in range(t):
    print(ans(i))
