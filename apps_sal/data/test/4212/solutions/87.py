import itertools
(n, m, q) = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(q)]
ans = 0
for A in itertools.combinations_with_replacement(range(1, m + 1), n):
    tmp = 0
    for i in range(q):
        (a, b, c, d) = abcd[i]
        if A[b - 1] - A[a - 1] == c:
            tmp += d
    ans = max(ans, tmp)
print(ans)
