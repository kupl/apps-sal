def can(i, j):
    return 0 < i < n - 1 and 0 < j < n - 1 and g[i][j + 1] and g[i + 1][j] and g[i][j - 1] and g[i - 1][j] and g[i][j]


def fill(i, j):
    g[i][j] = 0
    g[i + 1][j] = 0
    g[i - 1][j] = 0
    g[i][j + 1] = 0
    g[i][j - 1] = 0


n = int(input())
g = []
for _ in range(n):
    g.append([1 if x == '.' else 0 for x in input()])

for i in range(n):
    for j in range(n):
        if can(i, j):
            fill(i, j)

v = True

for i in range(n):
    for j in range(n):
        if g[i][j]:
            v = False

print("YES" if v else "NO")
