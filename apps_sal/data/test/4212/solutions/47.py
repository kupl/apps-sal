from itertools import combinations_with_replacement
(N, M, Q) = map(int, input().split())
ABCD = [list(map(int, input().split())) for _ in range(Q)]
ans = 0
for t in combinations_with_replacement(range(1, M + 1), N):
    an = 0
    for (a, b, c, d) in ABCD:
        if t[b - 1] - t[a - 1] == c:
            an += d
    if ans < an:
        ans = an
print(ans)
