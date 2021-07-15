n = int(input())
m = [input() for i in range(n)]
rows = [m[i].count('C') for i in range(n)]
columns = [0] * n
for j in range(n):
    for i in range(n):
        if m[i][j] == 'C':
            columns[j] += 1
ans = 0
for i in range(n):
    ans += (1 + (rows[i] - 1)) / 2 * (rows[i] - 1)
    ans += (1 + (columns[i] - 1)) / 2 * (columns[i] - 1)
print(int(ans))
