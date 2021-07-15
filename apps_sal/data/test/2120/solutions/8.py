n, m = [int(c) for c in input().split()]
v = [0] + [int(c) for c in input().split()]
chains = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = [int(c) for c in input().split()]
    chains[a].append(b)
    chains[b].append(a)

res = 0

for i in range(n):
    m = 0
    ind = 0
    for j in range(len(v)):
        if v[j] > m:
            m = v[j]
            ind = j

    res += sum([v[_] for _ in chains[ind]])

    v[ind] = 0

print(res)
