import itertools
N, M, Q = map(int, input().split())
ABCD = [[]for i in range(Q)]
for i in range(Q):
    ABCD[i] = list(map(int, input().split()))
ans = 0
for p in itertools.combinations_with_replacement([x for x in range(1, M + 1)], N):
    point = 0
    p = list(p)
    for a, b, c, d in ABCD:
        if p[b - 1] - p[a - 1] == c: point += d
    ans = max(ans, point)
print(ans)
