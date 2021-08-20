import itertools
(n, m) = list(map(int, input().split()))
path = [[False] * n for _ in range(n)]
for i in range(m):
    (a, b) = list(map(int, input().split()))
    a -= 1
    b -= 1
    path[a][b] = True
    path[b][a] = True
ans = 0
for i in itertools.permutations(list(range(n))):
    if i[0] == 0:
        for j in range(n):
            if j == n - 1:
                ans += 1
                break
            if not path[i[j]][i[j + 1]]:
                break
print(ans)
