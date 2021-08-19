n, m = list(map(int, input().lstrip().split(' ')))

a = list(map(int, input().lstrip().split(' ')))
c = list(map(int, input().lstrip().split(' ')))

costs = sorted([(i, cost) for i, cost in enumerate(c)],
               key=lambda x: (x[1], x[0]))
ci = 0
# print(costs)
for _ in range(m):
    cost = 0
    t, d = list(map(int, input().lstrip().split(' ')))
    t -= 1
    if a[t] > d:
        cost = d * c[t]
        a[t] -= d
    else:
        cost = a[t] * c[t]
        d -= a[t]
        a[t] = 0
        while d > 0 and ci < n:
            ai, _cost = costs[ci]
            if a[ai] > d:
                cost += d * _cost
                a[ai] -= d
                d = 0
            else:
                cost += a[ai] * _cost
                d -= a[ai]
                a[ai] = 0
                ci += 1
        if d > 0:
            cost = 0
    # print(a)
    print(cost)
