from itertools import combinations_with_replacement
(N, M, Q) = map(int, input().split())
ls = []
for _ in range(Q):
    (a, b, c, d) = map(int, input().split())
    ls.append((a - 1, b - 1, c, d))
ans = -1
for A in combinations_with_replacement(range(1, M + 1), r=N):
    sm = 0
    for (a, b, c, d) in ls:
        if A[b] - A[a] == c:
            sm += d
    ans = max(ans, sm)
print(ans)
