from itertools import combinations_with_replacement
(N, M, Q) = map(int, input().split())
ABCD = [list(map(int, input().split())) for _ in range(Q)]
point_max = 0
for A in combinations_with_replacement(range(1, M + 1), N):
    point = 0
    for (a, b, c, d) in ABCD:
        if A[b - 1] - A[a - 1] == c:
            point += d
    point_max = max(point, point_max)
print(point_max)
