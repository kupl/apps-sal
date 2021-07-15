3

from itertools import product, combinations


def process(case):
    regiment = map(rotate, homes, positions, case)
    return sum(case) if is_square(regiment) else float('inf')


def is_square(regiment):
    dists = list(map(lambda arg: dist_sq(*arg), combinations(regiment, 2)))
    dists.sort()
    return 0 < dists[0] == dists[3] < dists[4] == dists[5]


def dist_sq(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def rotate(home, position, step):
    (x, y), (a, b) = position, home
    if step == 0:
        return x, y
    if step == 1:
        return a-(y-b), b+(x-a)
    if step == 2:
        return a-(x-a), b-(y-b)
    if step == 3:
        return a+(y-b), b-(x-a)

n = int(input())
for r in range(n):
    positions = []
    homes = []
    for i in range(4):
        x, y, a, b = map(int, input().split())
        positions.append((x, y))
        homes.append((a, b))
    all_cases = product(range(4), repeat=4)
    result = min(map(process, all_cases))
    print(result if result != float('inf') else -1)
