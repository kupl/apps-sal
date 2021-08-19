(n, m) = map(int, input().split())
dist = [int(x) for x in input().split()]
taxi = [int(x) for x in input().split()]
dists = {}
d = []
for person in range(len(taxi)):
    if taxi[person]:
        dists[dist[person]] = 0
        d.append(dist[person])
start = 0
d.append(10 ** 11)
for person in range(len(taxi)):
    if taxi[person] == 0:
        while dist[person] > d[start + 1]:
            start += 1
        if abs(dist[person] - d[start]) <= abs(dist[person] - d[start + 1]):
            dists[d[start]] += 1
        else:
            dists[d[start + 1]] += 1
for d in dists:
    print(dists[d] if d != 10 ** 11 else '', end=' ')
