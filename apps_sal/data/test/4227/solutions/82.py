import itertools
(n, m) = map(int, input().split())
path = [[False] * n for _ in range(n)]
for i in range(m):
    (a, b) = map(int, input().split())
    path[a - 1][b - 1] = True
    path[b - 1][a - 1] = True
ans = 0
for i in itertools.permutations(range(n), n):
    if i[0] == 0:
        for j in range(n):
            if j == n - 1:
                ans += 1
                break
            if not path[i[j]][i[j + 1]]:
                break
print(ans)
