from itertools import combinations_with_replacement
(N, M, Q) = map(int, input().split())
abcd = [list(map(int, input().split())) for i in range(Q)]
m = [i for i in range(1, M + 1)]
A = [i for i in combinations_with_replacement(m, N) if i[0] == 1]
ans = 0
for i in A:
    an = 0
    for (a, b, c, d) in abcd:
        if i[b - 1] - i[a - 1] == c:
            an += d
    ans = max(ans, an)
print(ans)
