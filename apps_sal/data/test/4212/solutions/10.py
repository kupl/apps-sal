import itertools
N, M, Q = map(int, input().split())
ABCD_list = [[int(_) for _ in input().split()] for i in range(Q)]
combs = itertools.combinations_with_replacement(range(1, M + 1), N)
points = []
for comb in combs:
    A_list = list(comb)
    point = 0
    for inner in ABCD_list:
        if A_list[inner[1] - 1] - A_list[inner[0] - 1] == inner[2]:
            point += inner[3]
        points.append(point)
print(max(points))
