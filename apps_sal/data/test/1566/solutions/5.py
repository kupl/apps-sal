n = int(input())
s = [list(map(int, input())) for _ in range(n)]
INF = 10 ** 9
x1, x2, y1, y2 = INF, -INF, INF, -INF
for i in range(n):
    for j in range(n):
        if s[i][j] != 0:
            x1, x2, y1, y2 = min(x1, i), max(x2, i), min(y1, j), max(y2, j)
need = [[0] * n for _ in range(n)]
for i in range(x1, x2 + 1):
    for j in range(y1, y2 + 1):
        if i == x1 or i == x2:
            if j == y1 or j == y2:
                need[i][j] = 1
            else:
                need[i][j] = 2
        elif j == y1 or j == y2:
            need[i][j] = 2
        else:
            need[i][j] = 4
print("Yes" if need == s else "No")
