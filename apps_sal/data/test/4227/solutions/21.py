from itertools import permutations
(n, m) = map(int, input().split())
data = [[False] * n for i in range(n)]
for i in range(m):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    data[a][b] = True
    data[b][a] = True
ans = 0
for i in permutations(range(n), n):
    if i[0] == 0:
        for j in range(n):
            if j == n - 1:
                ans += 1
                break
            if not data[i[j]][i[j + 1]]:
                break
print(ans)
