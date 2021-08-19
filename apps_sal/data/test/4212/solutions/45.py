import itertools
(n, m, q) = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(q)]
v = list(itertools.combinations_with_replacement(range(1, m + 1), n))
ans = 0
for i in v:
    s = 0
    for (a, b, c, d) in abcd:
        if i[b - 1] - i[a - 1] == c:
            s += d
    ans = max(ans, s)
print(ans)
