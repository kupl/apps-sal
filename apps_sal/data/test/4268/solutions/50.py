import itertools

n, d = map(int, input().split())
points = []
for _ in range(n):
    point = list(map(int, input().split()))
    points.append(point)

combinations = list(itertools.combinations(points, 2))
dist_lists = []
ans = 0
for comb in combinations:
    A = comb[0]
    B = comb[1]

    tmp = 0
    for j in range(len(A)):
        tmp += (B[j] - A[j])**2

    distance = tmp**(0.5)

    if distance.is_integer():
        ans += 1
print(ans)
