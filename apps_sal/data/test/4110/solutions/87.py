from itertools import accumulate
from itertools import product

D, G = list(map(int, input().split()))
points = []
for i, _ in enumerate(list(range(D)), 1):
    P, C = list(map(int, input().split()))
    point = list(accumulate([100 * i] * P))
    point[-1] += C
    points.append(point)

ans = 1000
for completes in product(list(range(2)), repeat=D):
    solves = 0
    total = 0
    ex_points = []
    for comp, point in zip(completes, points):
        if comp:
            total += point[-1]
            solves += len(point)
        else:
            ex_points = point

    if total < G:
        for i, p in enumerate(ex_points, 1):
            if total + p >= G:
                solves += i
                break
        else:
            continue

    ans = min(ans, solves)

print(ans)
