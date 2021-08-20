from itertools import combinations_with_replacement
(N, M, Q) = map(int, input().split())
abcd = [tuple(map(int, input().split())) for _ in range(Q)]
ans = 0
for A in combinations_with_replacement(range(1, M + 1), N):
    score = 0
    for i in range(Q):
        (a, b, c, d) = abcd[i]
        if A[b - 1] - A[a - 1] == c:
            score += d
    ans = max(ans, score)
print(ans)
